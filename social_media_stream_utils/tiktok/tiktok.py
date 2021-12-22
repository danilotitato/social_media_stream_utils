from django.http import HttpResponse
from TikTokApi import TikTokApi

def last_post(request):
    user = request.GET.get('user')

    api = TikTokApi().get_instance()
    n_videos = 1

    last_post = api.by_username(user, count=n_videos)[0]

    last_post_link = 'tiktok.com/@{username}/video/{video_id}'.format(
        username = user,
        video_id = last_post['id'])

    return HttpResponse(last_post_link)