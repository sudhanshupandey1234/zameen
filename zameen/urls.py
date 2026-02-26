"""
URL configuration for zameen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from zameen import views
from django.conf.urls.static import static
from django.conf import settings
from login import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', views.login ,name="login"),
    
    path('room/<int:id>/', views.room, name= "room"),
    path('', views.base, name="base"),
    path('2bhk/', views.bhk2, name="bhk2"),
    path('About-Us/', views.AboutUs,name="aboutus"),
    path('3bhk/', views.bhk3, name="bhk3"),
    path('pg/', views.pg, name="pg"),
    path('bookingconfirm/<int:id>', views.bookingcon, name="bookingconfirm"),
    path('mybooking/', views.mybooking, name="mybooking"),
    path('more', views.more, name="more"),
    path('bookingform/<int:id>', views.bookingform, name="bookingform"),
    path('pauth/', include("login.urls")),

    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)