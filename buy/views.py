from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello World!")

def buyGold(request, num):
	res = "not"
	if num=="5":
		res = "ok"+"_50"
	if num=="48":
		res = "ok"+"_500"
	if num=="288":
		res = "ok"+"_3000"
	return HttpResponse(res)