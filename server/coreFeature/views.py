from django.http import HttpResponse
# from database import query
# from models import dictionary
# import json


def index(request):
	return HttpResponse("Got it")