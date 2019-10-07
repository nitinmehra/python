from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect


def check_user_login(function):
    def wrapper(request):
        if request.session.user_name != '':
            return function(request)
        else:
            raise PermissionDenied
    return wrapper

def user_not_login(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return view_func(request, *args, **kwargs)
        else:
            #raise PermissionDenied
            return redirect('index')
    return wrapper
