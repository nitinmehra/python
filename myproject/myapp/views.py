from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import hashlib 
from myapp.models import Users

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {'latest_question_list': 'latest_question_list'}
    return HttpResponse(template.render(context, request))
	

def about_us(request):
	#template = loader.get_template('about_us.html')
	context = {'latest_question_list': 'latest_question_list'}
	return render(request, "about_us.html", context)

def enrollment_page(request):
	template = loader.get_template('enrollment-form.html')
	context = {'latest_question_list': 'latest_question_list'}
	return HttpResponse(template.render(context, request))

def enrollment_from_submit(request):
	response_data = {'code' : 0, 'status' : 'fail', 'msg' : 'not submitted'}
	if request.POST.get('formname') == 'create_user':
		password = hashlib.md5(request.POST['password'].encode()).hexdigest()
		create_user = Users(
				user_name = request.POST['name'],
				user_phone = request.POST['phone'],
				user_email = request.POST['email'],
				user_password = password
			)
		create_user.save()
		response_data = {'code' : 1, 'status' : 'success', 'msg' : 'User created successfuly'}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def users_list(request):
	template = loader.get_template('users_list.html')
	fetch_users = Users.objects.all()
	return HttpResponse(template.render({'users_list' : fetch_users}, request))
	
def user_login(request):
	response_data = {'code' : 0, 'status' : 'fail', 'msg' : request}
	if request.POST.get('formname') == 'user_login':
		user_email = request.POST['user_email']
		password = hashlib.md5(request.POST['user_password'].encode()).hexdigest()
		result = check_credentials(user_email, password)
		response_data = {'code' : 1, 'status' : 'success', 'msg' : result}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def check_credentials(email, password):
	user_email = email
	pwd = password
	user_ob = Users.objects.filter(user_email=user_email,user_password=pwd).values()
	if user_ob.exists():
		return list(user_ob)
	else:
		return False
