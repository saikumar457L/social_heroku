from django.urls import path



from .views import image_create,image_detail

app_name = "images"

urlpatterns = [
    path("image-bookmark/",image_create, name ="image_bookmark"),
    path("detail/<int:id>/<slug:slug>/",image_detail, name="image_detail"),
    
]
