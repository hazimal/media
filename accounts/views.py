from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.http import HttpResponse
from django.template import loader
from .models import Course
# Create your views here.
MESSAGE_TAGS = {
    messages.SUCCESS: 'alert alert-success',
}


def login_view(request):
    title = 'Login'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if user.is_authenticated:
            messages.success(request, 'You are login successfully ' + str(request.user),
                             extra_tags='alert alert-success')
        else:
            messages.error(request, "Error")
        return redirect('index')
    return render(request, 'login.html', {'form': form, 'title': title})


def register_view(request):
    title = 'Register'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('list')

    context = {
        'form': form,
        'title': title
    }
    return render(request, 'form.html', context)


def index(request):
    template = loader.get_template("index.html")
    context = {"hello": "hello"}
    return HttpResponse(template.render(context, request))

def course_view(request):
    list_course = Course.objects.filter(name=request.user)
    return render(request, 'courses.html', {'data': list_course})
