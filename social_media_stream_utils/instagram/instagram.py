from django.http import HttpResponse
import instaloader

def instawar(request):
    current_user = request.GET.get('current_user')
    rival_user = request.GET.get('rival_user')
    winning_emote = request.GET.get('winning_emote', '')
    losing_emote = request.GET.get('losing_emote', '')

    current_user_followers = get_profile_followers(current_user)
    rival_user_followers = get_profile_followers(rival_user)

    emote = winning_emote if current_user_followers > rival_user_followers else losing_emote

    response = '{user1} has {followers1} followers vs. {followers2} from {user2} {emote}'.format(user1 = current_user, followers1 = current_user_followers, user2 = rival_user, followers2 = rival_user_followers, emote = emote)

    return HttpResponse(response)

def last_post(request):
    user = request.GET.get('user')

    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, user)

    last_post = next(profile.get_posts())

    last_post_link = 'instagram.com/p/{post_id}'.format(post_id = last_post.shortcode)

    return HttpResponse(last_post_link)

def get_profile_followers(profile_name):
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, profile_name)

    return profile.followers