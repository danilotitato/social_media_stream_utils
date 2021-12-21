from django.urls import path

from .instagram import instagram

urlpatterns = [
    path('instawar/', instagram.instawar, name="instawar"),
    path('last_insta_post/', instagram.last_post, name="last_insta_post"),
]
