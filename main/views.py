
from django.shortcuts import render
from .models import * 
from django.http import JsonResponse, HttpResponse
import urllib
from django.core.files.storage import default_storage
from catering.settings import * 
import json
from django.template.loader import render_to_string
import os

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def index(request):
    template = "main/index.html"
    somelist = [1,3,4,5,6,7]
    context = {
        'somelist': somelist,
    }
    return render(request, template, context)

def products(request):
    template = "main/products.html"
    somelist = [1,3,4,5,6,7]
    context = {
        'somelist': somelist,
    }
    return render(request, template, context)

def contact_form(request):
    is_sended = True
    phone = request.GET['phone']

    try:
        send_mail(
            'Заявка на обратный звонок c сайта кейтеринга',
            'Номер телефона: {} '.format(phone),
            settings.EMAIL_HOST_USER,
            [
            'worlddelete0@mail.ru', 
            ],
            )
    except:
        pass

    return JsonResponse({
        'is_sended': is_sended,
    })