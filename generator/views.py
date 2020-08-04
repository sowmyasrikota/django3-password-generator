from django.shortcuts import render
from django.http import HttpResponse

import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html',{'name':'sowmya'})
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thepassword = ''
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('speacial'):
        characters.extend(list('@#$%^&*()!+/*-'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')
