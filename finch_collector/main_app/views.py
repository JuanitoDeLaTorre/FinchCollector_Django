from django.shortcuts import render, redirect
from .models import Camera, Photo, Gear
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import PhotoForm, GearForm


# Create your views here.


def home(request):
    all_cameras = Camera.objects.filter()

    return render(request, "index.html", {"cameras": all_cameras})


def about(request):
    return render(request, "about.html")


def detail(request, id):
    photos = Photo.objects.filter(camera_id=id)
    camera = Camera.objects.get(id=id)
    photo_form = PhotoForm()

    return render(
        request,
        "detail.html",
        {"camera": camera, "photo_form": photo_form, "photos": photos},
    )


class CreateCamera(CreateView):
    model = Camera
    fields = ["name", "price", "resolution", "image"]


class UpdateCamera(UpdateView):
    model = Camera
    fields = ["name", "price", "resolution", "image"]


class DeleteCamera(DeleteView):
    model = Camera

    success_url = "/"


def add_photo(request, cam_id):
    form = PhotoForm(request.POST)

    if form.is_valid():
        new_photo = form.save(commit=False)
        new_photo.camera_id = cam_id
        new_photo.save()

    return redirect("detail", id=cam_id)


class PhotoDelete(DeleteView):
    model = Photo
    success_url = "/"


# def list_gear(request):
#     all_gear = Gear.objects.filter()
#     return render(request, "list_gear.html", {"gear": all_gear})


# def create_gear(request):
#     if request.method == "POST":
#         new_gear = GearForm(request.POST)
#         print(new_gear)
#         new_gear.save()
#         return redirect("list_gear")
#     form = GearForm()
#     return render(request, "create_gear.html", {"form": form})


class CreateGear(CreateView):
    model = Gear
    fields = "__all__"


class ListGear(ListView):
    model = Gear
