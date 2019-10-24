import re
from django import template

register = template.Library()

@register.filter
def make_link(article):
    # content = article.content + ' '
    content = article.content
    hashtags = article.hashtags.all()
    for hashtag in hashtags:
        # content = content.replace(hashtag.content + ' ', f'<a href="/hashtags/{hashtag.pk}/">{hashtag.content}</a>')
        content = re.sub(f'{hashtag.content}\\b' , f'<a href="/hashtags/{hashtag.pk}/">{hashtag.content}</a>', content)
    return content
