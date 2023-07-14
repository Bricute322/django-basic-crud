from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GrocerySerializers
from .models import Grocery
from .utils import generate_uuid

class CreateGroceryNameViews(APIView):
    def post(self, request):
        serializer = GrocerySerializers(data=request.data)
        data = {}
        errors = {}
        status = None
        message = None

        if serializer.is_valid():
            uid = generate_uuid()
            grocery = Grocery.objects.create(
                id = uid,
                name = request.data['name'],
                price = request.data['price']
            )
            grocery = Grocery.objects.filter(id=uid).values('id','name','price')
            data = grocery
            errors = serializer.errors
            status = '200'
            message = 'Sucessfully Item Created'
            return Response({"message": message, "data": data, "status": status, "errors": errors})
        errors = serializer.errors
        status = '400'
        return Response({"message": "error!", "status": status, "errors": serializer.errors})
    
class DisplayGroceryItemViews(APIView):
    def get(self, request):
        data = {}
        errors = {}
        status = None
        message = None

        grocery = Grocery.objects.all().values('id', 'name', 'price')
        data = grocery
        message = 'Success'
        status = '200' 
        return Response({"message": message, "data": data, "status": status, "errors": errors})

            # grocery = Grocery.object.filter
# Create your views here.
