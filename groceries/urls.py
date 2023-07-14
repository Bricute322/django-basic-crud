from django.contrib import admin
from django.urls import path
from core.views import CreateGroceryNameViews, DisplayGroceryItemViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grocery/create/', CreateGroceryNameViews.as_view(),name='create-grocery'),
    path('grocery/display/', DisplayGroceryItemViews.as_view(),name='display-grocery')
]
