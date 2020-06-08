from django.db import models

from django.conf import settings

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # In place of OneToOneField we can alse use ForeignKey

    date_of_birth = models.DateField(blank=True,null=True)

    photo = models.ImageField(default="avatar.png",upload_to="users/%y/%m/%d",blank=True,null=True)

    def __str__ (self):
        return "Profile for user {}".format(self.user.username)
