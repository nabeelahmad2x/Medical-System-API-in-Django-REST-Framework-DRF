from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views


router = DefaultRouter()
router.register(r'doctors', views.DoctorViewSet, basename='doctor')
router.register(r'patients', views.PatientViewSet, basename='patient')


urlpatterns = [
    # path('home/', views.Home.as_view()),
    path('', include(router.urls)),
]

