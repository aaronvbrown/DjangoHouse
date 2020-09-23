from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(reequest):
    return HttpResponse("Hello, you're at the new SCHEDULE app.")
