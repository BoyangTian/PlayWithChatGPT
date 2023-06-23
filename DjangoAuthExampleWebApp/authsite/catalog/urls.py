from django.urls import path

from . import views

# Since we move the "template" folder out the current folder, we need to change html path
app_name = "catalog"

urlpatterns = [
    path("", views.index, name="index"),
]