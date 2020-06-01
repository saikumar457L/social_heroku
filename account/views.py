from django.shortcuts import render

from django.contrib.auth.decorators import login_required #import login_required

from django.conf import settings

from .forms import UserRegistrationForm,ProfileEditForm,UserEditForm

from .models import Profile

from django.contrib import messages

# Create your views here.


@login_required
def dashboard(request):

    return render (request,"site/dashboard.html",{"section":"dashboard"})



def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user) # remember this one, here user is the variable in the profile model,we assiginig the new_user to user variable

            return render(request,"account/account_register_complete.html",{'new_user':new_user})

    else:
        user_form = UserRegistrationForm()

    return render(request,"account/account_register.html",{"user_form":user_form})


@login_required
def profile_edit(request):

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)

        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request,"Profile updated successfully.")

        else:
            messages.error(request,"Something went wrong, please try again.")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render (request,"account/profile_edit.html",{"user_form":user_form,"profile_form":profile_form})
