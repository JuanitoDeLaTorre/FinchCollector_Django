from django.forms import ModelForm
from .models import Photo, Gear


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ["name", "url"]


class GearForm(ModelForm):
    class Meta:
        model = Gear
        fields = "__all__"
