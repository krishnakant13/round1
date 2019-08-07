from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import random
from django.contrib.auth import login
from .models import Questions
from django.urls import reverse


# Create your views here.


def index1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email_id = request.POST.get('email')
        phno = request.POST.get('phno')
        user = User.objects.create_user(username=username, password=password, email=email_id)
        login(request, user)
        return redirect(reverse('second_page'))

    elif request.method == 'GET':
        return render(request, 'signup.html')


def index2(request):
    k=0
    qno = random.randint(1, 4)
    questions = Questions.objects.get(pk=qno)
    ans = request.POST.get('option1', 'option2', 'option3', 'option4')
    if ans == Questions.answer.get(pk=qno):
        k = k + 1
    return render(request, 'Question.html', {'question': questions})
