from django.urls import path



from .views import image_create

app_name = "images"

urlpatterns = [
    path("image-bookmark/",image_create, name ="image_bookmark")
]
