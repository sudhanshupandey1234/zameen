from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regi/', views.registerv, name="registerv"),
    
    path('log/', views.loginv, name="loginv"),

]