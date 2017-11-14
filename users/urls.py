from django.conf.urls import url

import users.views as views

urlpatterns = [
    url(r'^(.*)', views.specific_user),
]
