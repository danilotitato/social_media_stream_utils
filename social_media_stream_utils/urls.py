from django.urls import path

from .instagram import instagram
from .tiktok import tiktok

urlpatterns = [
    path('instawar/', instagram.instawar, name="instawar"),
    path('last_insta_post/', instagram.last_post, name="last_insta_post"),
    path('last_tiktok_post/', tiktok.last_post, name="last_tiktok_post"),
]
