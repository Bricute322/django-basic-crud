from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GrocerySerializers
from .models import Grocery
from .utils import generate_uuid
from .static_messages import ok, bad_request
from django.http import Http404
from django.shortcuts import get_object_or_404


class CreateGroceryNameViews(APIView):
    def post(self, request):
        serializer = GrocerySerializers(data=request.data)
        data, errors, status, message = {}, {}, None, None
        if serializer.is_valid():
            name = request.data['name']
            if Grocery.objects.filter(name=name).exists():
                message = f"The name already exists in the database."
                status = bad_request
            else:
                uid = generate_uuid()
                grocery = Grocery.objects.create(
                    id=uid,
                    name=request.data['name'],
                    price=request.data['price'],
                    description=request.data['description']
                )
                grocery = Grocery.objects.filter(
                    id=uid).values('id', 'name', 'price', 'description')
                data = grocery
                errors = serializer.errors
                status = ok
                message = 'Sucessfully Item Created'
                return Response({"message": message, "data": data, "status": status, "errors": errors})
        else:
            errors = serializer.errors
            status = bad_request
            message = message
        return Response({"message": message, "status": status, "errors": serializer.errors})


class DisplayGroceryItemViews(APIView):
    def get(self, request):
        data, errors, status, message = {}, {}, None, None
        grocery = Grocery.objects.all().values('id', 'name', 'price', 'description')
        data = grocery
        message = 'Success'
        status = ok
        return Response({"message": message, "data": data, "status": status, "errors": errors})


class UpdateGroceryItemViews(APIView):
    def put(self, request, *args, **kwargs):
        data, errors, status, message = {}, {}, None, None
        grocery_id = request.query_params['id']
        grocery = Grocery.objects.filter(id=grocery_id).get()
        serializer = GrocerySerializers(
            instance=grocery, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            message = 'Successfuly Item Updated'
            status = ok
            errors = serializer.errors
            return Response({"message": message, "data": data, "status": status, "errors": errors})

        errors = serializer.errors
        status = bad_request
        return Response({"message": "error!", "status": status, "errors": serializer.errors})


class DeleteGroceryItemViews(APIView):
    def delete(self, request, *args, **kwargs):
        data, errors, status, message = {}, {}, None, None
        grocery_id = request.query_params['id']

        if grocery_id:
            grocery = get_object_or_404(Grocery, id=grocery_id)
            grocery.delete()
            message = 'Successfully deleted the item'
            status = 'ok'
            return Response({"message": message, "data": data, "status": status, "errors": errors})
        else:
            raise Http404("Grocery ID parameter is missing")

        # grocery = Grocery.object.filter
# Create your views here.
