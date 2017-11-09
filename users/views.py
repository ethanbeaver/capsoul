# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET

from database.models import User


@require_http_methods(["GET", "POST"])
def all_users(request):
    if request.method == 'GET':
        all_users = User.objects.all().values('user_name', 'first_name', 'last_name')
        return JsonResponse({'users': list(all_users)}, status=200)
    else:
        updated_fields = {'user_name': request.user.user_name}
        for field in request.POST:
            updated_fields[field] = request.POST.get(field)
        current_user = User(**updated_fields)
        current_user.save()
        return JsonResponse({"status": "resource created"}, status=200)


@require_GET
def specific_user(request, uname):
    user = User.objects.filter(user_name=uname).values()
    return JsonResponse({'users': list(user)}, status=200)
