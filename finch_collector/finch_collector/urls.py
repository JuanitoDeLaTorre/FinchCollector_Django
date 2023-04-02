"""finch_collector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from main_app import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("camera/<int:id>", views.detail, name="detail"),
    path("camera/create", views.CreateCamera.as_view(), name="camera_create"),
    path("camera/update/<int:pk>", views.UpdateCamera.as_view(), name="camera_update"),
    path("camera/delete/<int:pk>", views.DeleteCamera.as_view(), name="camera_delete"),
    path("photo/add/<int:cam_id>", views.add_photo, name="photo_add"),
    path("photo/delete/<int:pk>", views.PhotoDelete.as_view(), name="delete_photo"),
    path("gear/", views.ListGear.as_view(), name="list_gear"),
    path("gear/new", views.CreateGear.as_view(), name="gear_create"),
    path(
        "camera/<int:cam_id>/assoc_gear/<int:gear_id>/",
        views.assoc_gear,
        name="assoc_gear",
    ),
    path(
        "camera/<int:cam_id>/unassoc_gear/<int:gear_id>/",
        views.unassoc_gear,
        name="unassoc_gear",
    ),
]
