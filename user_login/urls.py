from django.urls import path
from user_login import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    #path('login/', views.LoginView.as_view(), name='login'),
    #path ('refresh/', views.RefreshView.as_view(), name='refresh')
]
