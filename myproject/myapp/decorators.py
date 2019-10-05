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

def check_user_not_login(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.user_id == '':
            return view_func(request, *args, **kwargs)
        else:
            #raise PermissionDenied
            return render(request, "index")
    return wrapper
