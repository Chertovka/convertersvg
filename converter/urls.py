from django.urls import path
from .views import upload_file

urlpatterns = [
    path('', upload_file, name = "upload_file"),
    # path('upload/', upload_file2, name = "upload_file2"),
]