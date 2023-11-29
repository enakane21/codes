from django.shortcuts import render
# The from keyword allows importing of neccesary Classes, methods, and other items needed in our application from the "django.http" package while the import keyword defines what are we importing from the package
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello from the views.py file")
