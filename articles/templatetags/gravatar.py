import hashlib
from django import template

register = template.Library()

@register.filter
def makehash(user):
    email = user.email
    social_user = user.socialaccount_set.all().first()
    if social_user:
        return social_user.extra_data.get('properties').get('profile_image')
    return 'https://www.gravatar.com/avatar/' + hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest() + '?size=25'


@register.filter
def profile(email):
    return 'https://www.gravatar.com/avatar/' + hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest() + '?size=300'