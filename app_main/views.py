from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import DataAnnotation, Annotator
from django.contrib import messages
import random
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == 'POST':
        first_bn = request.POST['FirstNameBn']
        middle_bn = request.POST['MiddleNameBn']
        last_bn = request.POST['LastNameBn']

        first_en = request.POST['FirstNameEn']
        middle_en = request.POST['MiddleNameEn']
        last_en = request.POST['LastNameEn']

        audio = request.FILES.get('audio_file')

        if audio is None:
            print('No audio')

        annotator, created = Annotator.objects.get_or_create(user=request.user)
        annotator.count += 1
        messages.info(request, annotator.count)
        annotator.save()

        dataAnnotation = DataAnnotation(first_name_bn=first_bn, middle_name_bn=middle_bn, last_name_bn=last_bn,
                                        first_name_en=first_en, middle_name_en=middle_en, last_name_en=last_en,
                                        audio=audio, annotator=annotator)
        dataAnnotation.save()

        return redirect('home')

    return render(request, 'home.html')


@login_required
def Dashboard(request):
    total_audio = DataAnnotation.objects.count()
    annotators = Annotator.objects.all().order_by('-count')
    return render(request, 'dashboard.html', {'total_audio': total_audio, 'annotators': annotators})


def Login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        messages.info(request, 'Invalid Username/Password')
        return render(request, 'login.html')

    return render(request, 'login.html')


def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            auth_login(request, user)
            return redirect('home')  # Redirect to a success page
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, "An error occurred: " + str(e))

    return render(request, 'register.html')


def logout_user(request):
    logout(request)
    return redirect("home")
