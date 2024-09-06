from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'appointments', views.AppointmentViewSet, basename='appointment')
router.register(r'encounters', views.EncounterViewSet, basename='encounter')

urlpatterns = [
    path('', include(router.urls)),
    path('cancel/<int:pk>/', views.AppointmentViewSet.as_view({'get': 'cancel_appointment'})),
    # view commented out not in use..
    # path('encounter-details/<int:encounter_id>/', views.get_encounter_details, name='encounter-details'),
]
