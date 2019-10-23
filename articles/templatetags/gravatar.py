import hashlib
from django import template

register = template.Library()

@register.filter
def makehash(email):
    return 'https://www.gravatar.com/avatar/' + hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest() + '?size=25'

@register.filter
def profile(email):
    return 'https://www.gravatar.com/avatar/' + hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest() + '?size=300'