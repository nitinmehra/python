from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
import json
import hashlib 
from myapp.models import Users

from .forms import EnromentForm

# Create your views here.

def index(request):
	return render(request, "index.html", {'latest_question_list': 'latest_question_list'})
	
def about_us(request):
	#template = loader.get_template('about_us.html')
	context = {'latest_question_list': 'latest_question_list'}
	return render(request, "about_us.html", context)

def user_enrollment(request):
	# if this is a POST request we need to process the form data
	print(request)
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = EnromentForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
			#if request.POST.get('formname') == 'create_user':
			password = hashlib.md5(request.POST['user_password'].encode()).hexdigest()
			create_user = Users(
					user_name = request.POST['user_name'],
					user_phone = request.POST['user_phone'],
					user_email = request.POST['user_email'],
					user_password = password
				)
			create_user.save()
			return redirect('users_list')
			'''response_data = {'code' : 1, 'status' : 'success', 'msg' : 'User created successfuly'}
			print(response_data)
			template = loader.get_template('enrollment-form.html')
			return HttpResponse(template.render({'users_list' : fetch_users}, request))'''
	# if a GET (or any other method) we'll create a blank form
	else:
		form = EnromentForm()
		return render(request, "enrollment-form.html", {'form' : form})


def enrollment_from_submit(request):
	'''response_data = {'code' : 0, 'status' : 'fail', 'msg' : 'not submitted'}
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = Enroment_form(request.POST)
        # check whether it's valid:
		if form.is_valid():
			#if request.POST.get('formname') == 'create_user':
			password = hashlib.md5(request.POST['password'].encode()).hexdigest()
			create_user = Users(
					user_name = request.POST['name'],
					user_phone = request.POST['phone'],
					user_email = request.POST['email'],
					user_password = password
				)
			create_user.save()
			response_data = {'code' : 1, 'status' : 'success', 'msg' : 'User created successfuly'}
			# if a GET (or any other method) we'll create a blank form
	else:
		form = Enroment_form()

	return HttpResponse(json.dumps(response_data), content_type="application/json")'''

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
		if result == False:
			response_data = {'code' : 1, 'status' : 'success', 'msg' : 'Invalid credentials'}
		else:
			response_data = {'code' : 1, 'status' : 'success', 'msg' : 'True'}
			
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def check_credentials(email, password):
	user_email = email
	pwd = password
	user_ob = Users.objects.filter(user_email=user_email,user_password=pwd).values()
	if user_ob.exists():
		return list(user_ob)
	else:
		return False
