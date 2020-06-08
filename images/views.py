from django.shortcuts import render

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ImageCreationForm

from django.shortcuts import get_object_or_404
from .models import Image

# Create your views here.


@login_required
def image_create(request):

    if request.method == "POST":

        form = ImageCreationForm(data = request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            new_item = form.save(commit=False)
            new_item.user = request.user

            new_item.save()

            messages.success(request,"Image added successfully")

            # redirect to new created item detail view

            return redirect (new_item.get_absolute_url())

    else:
        form = ImageCreationForm(data=request.GET) # must insert parameter  as data=request.GET

    return render(request,"image/create.html",{"section":"images","form":form})


def image_detail(request,id,slug):
    image = get_object_or_404(Image,id=id,slug=slug)
    return render (request,"image/image_detail.html",{'section':'images','image':image})
