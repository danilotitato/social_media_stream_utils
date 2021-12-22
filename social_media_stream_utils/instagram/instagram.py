from django.http import HttpResponse
import instaloader

def instawar(request):
    current_user = request.GET.get('current_user')
    rival_user = request.GET.get('rival_user')
    current_alias = request.GET.get('current_alias',current_user)
    rival_alias = request.GET.get('rival_alias', rival_user)
    winning_emote = request.GET.get('winning_emote', '')
    losing_emote = request.GET.get('losing_emote', '')

    current_user_followers = get_profile_followers(current_user)
    rival_user_followers = get_profile_followers(rival_user)

    follower_diff = rival_user_followers - current_user_followers
    diff_response = ' Need {remaining} followers more!'.format(remaining = follower_diff) if follower_diff > 0 else ''
    emote = losing_emote if follower_diff >= 0 else winning_emote

    response = '{alias1} has {followers1} followers vs. {followers2} from {alias2} on instagram {emote}{diff} Follow me on instagram.com/{user1}'.format(
        alias1 = current_alias,
        followers1 = current_user_followers,
        alias2 = rival_alias,
        followers2 = rival_user_followers,
        emote = emote,
        diff = diff_response,
        user1 = current_user)

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