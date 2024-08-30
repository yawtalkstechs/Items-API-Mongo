from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ItemsViewset

router = DefaultRouter()

router.register(r'items', ItemsViewset, basename='items')

urlpatterns = [
    path('', include(router.urls))
]