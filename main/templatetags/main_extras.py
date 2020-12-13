from django import template

from main.models import *

register = template.Library()

@register.simple_tag
def modify_imgsrc(imgsrc):
    if imgsrc == None:
        return 'https://placehold.it/500x500'
    else:
        img = imgsrc.url.replace('/static/images/products/', '')
        img = imgsrc.url.replace('static/images/products/', '')
        return '/static/images/products/' + img
    # return imgsrc.replace('static/', '')







