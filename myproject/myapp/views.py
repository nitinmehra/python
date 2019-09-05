from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from myapp.models import Users

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {'latest_question_list': 'latest_question_list'}
    return HttpResponse(template.render(context, request))

def about_us(request):
	template = loader.get_template('about_us.html')
	context = {'latest_question_list': 'latest_question_list'}
	return HttpResponse(template.render(context, request))

def enrollment_page(request):
	template = loader.get_template('enrollment-form.html')
	context = {'latest_question_list': 'latest_question_list'}
	return HttpResponse(template.render(context, request))

def enrollment_from_submit(request):
	response_data = {'code' : 0, 'status' : 'fail', 'msg' : 'not submitted'}
	if request.POST.get('formname') == 'create_user':
		create_user = Users(
				user_name = request.POST['name'],
				user_phone = request.POST['phone'],
				user_email = request.POST['email']
			)
		create_user.save()
		response_data = {'code' : 1, 'status' : 'success', 'msg' : 'User created successfuly'}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def users_list(request):
	template = loader.get_template('users_list.html')
	fetch_users = Users.objects.all()
	#return HttpResponse(template.render(json.dumps({'users_data' : list(fetch_users)}), request))