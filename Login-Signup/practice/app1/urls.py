from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexview,name="index"),
    path('register',views.registerview,name="register"),
    path('login',views.loginview,name="login"),
    path('dashboard',views.dashboardview,name="dashboard"),
    path('logout',views.logoutview,name="logout"),
]