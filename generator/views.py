from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',9))
    password = ''
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        chars.extend(list('123456789'))
    if request.GET.get('special'):
        chars.extend('`~!@#$%^&*()_=<>?/\|}{[],.')

    for x in range(length):
        password += random.choice(chars)


    return render(request,'generator/password.html', {'password':password})
def about(request):
    return render(request,'generator/about.html')
