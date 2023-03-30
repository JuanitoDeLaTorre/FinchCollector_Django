from django.shortcuts import render, redirect
from .models import Camera, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PhotoForm


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
    fields = "__all__"


class UpdateCamera(UpdateView):
    model = Camera
    fields = "__all__"


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
