# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


# Create your views here.

def index(request):
    counter = request.session.get('counter', 0)
    request.session['counter'] = counter + 1
    unique_id = get_random_string(length=14)
    # request.session["random_word"] = { "word" : get_random_string(length=14) }
    dictionary = {
        'randomstring': unique_id,
    }
    return render(request, 'randWord/index.html', dictionary)

def reset(request):
    request.session.clear()
    return redirect('/')
    