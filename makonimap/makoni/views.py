from django.shortcuts import render

from .map import Map

# Create your views here.


def activate(request):
    if request.method == "GET":
        map_app = Map("AIzaSyBMglCkfaEDPOIdLPfCEfSUVI6rl1ONQNQ")

