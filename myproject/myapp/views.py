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
			#return HttpResponse(template.render({'users_list' : fetch_users}, request))
	# if a GET (or any other method) we'll create a blank form
	else:
		form = EnromentForm()
		return render(request, "enrollment-form.html", {'form' : form})


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
			request.session['user_id'] = result['id']
			request.session['user_name'] = result['user_name']
			response_data = {'code' : 1, 'status' : 'success', 'msg' : 'True', 'data':result}
			
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def check_credentials(email, password):
	user_email = email
	pwd = password
	try:
	    user_ob = Users.objects.filter(user_email=user_email,user_password=pwd).get().as_dict()
	except ObjectDoesNotExist:
		user_ob = False
	except MultipleObjectsReturned:
		user_ob = False
	return user_ob

	
