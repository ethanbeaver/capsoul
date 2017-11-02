# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model

from rest_framework.authtoken.models import Token

# Get the User Model
UserModel = get_user_model()

# Create your views here.

def login(request, *args, **kwargs):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed",status=405)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        response = JsonResponse({'result':'success','token':token.key})
        response.set_cookie('session', token.key)
    else:
        response =  JsonResponse({'result':'error'})
    return response

def register(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed",status=405)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password, is_active=True)
    if user is not None:
        response = JsonResponse({'result':'error', 'description':'User already exists'})
    else:
        user = UserModel.objects.create_user(username, password)
        token, created = Token.objects.get_or_create(user=user)
        response = JsonResponse({'result':'success','description':'User has been created','token':token.key})
        response.set_cookie('session', token.key)
    return response

def logout(request):
    response = JsonResponse({'result':'Successfully logged out'})
    response.delete_cookie('session')
    return response

