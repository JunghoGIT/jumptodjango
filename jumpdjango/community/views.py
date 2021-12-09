from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("윤정호의 첫 django page")