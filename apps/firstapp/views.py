from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'firstapp/index.html')
