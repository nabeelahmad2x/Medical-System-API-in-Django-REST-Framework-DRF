from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'appointments', views.AppointmentViewSet, basename='appointment')
router.register(r'encounters', views.EncounterViewSet, basename='encounter')

urlpatterns = [
    path('', include(router.urls)),
    path('encounter-details/<int:encounter_id>/', views.get_encounter_details, name='encounter-details'),
]
