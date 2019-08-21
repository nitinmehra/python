from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {'latest_question_list': 'latest_question_list'}
    return HttpResponse(template.render(context, request))

def about_us(request):
	template = loader.get_template('about_us.html')
	context = {'latest_question_list': 'latest_question_list'}
	return HttpResponse(template.render(context, request))