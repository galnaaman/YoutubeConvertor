from django.urls import path , include
from downloader import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("download/", views.download_vid, name="download")
]
