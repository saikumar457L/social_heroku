from django import forms

from .models import Image

from django.utils.text import slugify
from urllib import request
from django.core.files.base import ContentFile


class ImageCreationForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ["title","description","url"]

        widgets = {
            "url":forms.HiddenInput, # the url is render as hidden field
        }

    def clean_url(self):
        url = self.cleaned_data["url"]
        valid_extensions = ["jpg","jpeg"]
        extension_url = url.rsplit(".",1)[1].lower()

        if extension_url not in valid_extensions:
            raise forms.ValidationError("The given URL does not match valid image extensions")

        return url

    def save(self,force_insert=False,force_update=False,commit=True):

        image = super(ImageCreationForm,self).save(commit=False)
        image_url = self.cleaned_data["url"]
        image_name = "{}.{}".format(slugify(image.title),image_url.rsplit(".", 1)[1].lower())

        # downloading the image

        response = request.urlopen(image_url)
        image.image.save(image_name,ContentFile(response.read()),save=False)

        if commit:
            image.save()
        return image
