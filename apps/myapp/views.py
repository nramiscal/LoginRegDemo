from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    # print('inside register method in views')
    result = User.objects.reg_validator(request.POST)
    # print('back inside register in views')
    # print(result)
    if len(result) > 0:
        for key, value in result.items():
            # messages.error(request, value)
            messages.add_message(request, messages.ERROR, value)
        return redirect('/')
    else: # passed validations
        # create the user (add to database)
        hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(fname=request.POST['fname'], lname=request.POST['lname'], email = request.POST['email'], password=hash.decode())
        # print(user.id)
        # save their id in session
        request.session['userid'] = user.id
        # redirect to success page/dashboard
        return redirect('/success')

def success(request):
    user = User.objects.get(id=request.session['userid'])
    context = {
        'user': user
    }
    return render(request, 'success.html', context)
