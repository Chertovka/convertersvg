from django.urls import path
from .views import upload_file, index

urlpatterns = [
    path('', index, name = "index"),
    # path('upload/', upload_file, name = "upload_file"),
]