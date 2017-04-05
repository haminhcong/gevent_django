from django.shortcuts import render
import run_server
# Create your views here.
from django.http import HttpResponse


def index(request):
    x = run_server.global_object
    for i in range(1,50000000):
            run_server.global_object += 1

    return HttpResponse("Hello, world. You're at the polls index."+str(run_server.global_object))
