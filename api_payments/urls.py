from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'payments', views.PaymentHistoryViewSet, basename='paymenthistory')

urlpatterns = [
    path('', include(router.urls)),
]

