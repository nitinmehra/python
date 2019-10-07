from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect


def login_required(function):
    def wrapper(request):
        if 'user_id' in request.session:
            return function(request)
        else:
            raise PermissionDenied
    return wrapper

def login_not_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return view_func(request, *args, **kwargs)
        else:
            #raise PermissionDenied
            return redirect('index')
    return wrapper
