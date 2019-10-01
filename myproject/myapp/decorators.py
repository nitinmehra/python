from django.core.exceptions import PermissionDenied


def check_user_login(function):
    def wrapper(request):
        if request.session.user_name != '':
            return function(request)
        else:
            raise PermissionDenied
    return wrapper

def check_user_not_login(function):
    def wrapper(request):
        if request.session.user_name == '':
            return function(request)
        else:
            raise PermissionDenied
    return wrapper
