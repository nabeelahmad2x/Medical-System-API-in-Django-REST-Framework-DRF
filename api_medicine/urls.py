from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'medicines', views.MedicineViewSet, basename='medicine')


urlpatterns = [
    path('', include(router.urls)),
]

