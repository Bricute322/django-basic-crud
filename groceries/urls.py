from django.contrib import admin
from django.urls import path
from core.views import CreateGroceryNameViews, DisplayGroceryItemViews, UpdateGroceryItemViews, DeleteGroceryItemViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grocery/delete/', DeleteGroceryItemViews.as_view(), name='delete-grocery'),
    path('grocery/create/', CreateGroceryNameViews.as_view(), name='create-grocery'),
    path('grocery/display/', DisplayGroceryItemViews.as_view(),
         name='display-grocery'),
    path('grocery/update/', UpdateGroceryItemViews.as_view(), name='update-grocery')
]
