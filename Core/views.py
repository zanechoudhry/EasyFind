from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Core.forms import LoginForm, JoinForm, UserProfile, EditSettings

@login_required(login_url='/login/')
def home(request):
    return render(request, "Core/home.html")
def about(request):
    return render(request, "Core/about.html")
def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            user = join_form.save()
            UserProfile.objects.create(
                user=user, first_name=user.first_name, last_name=user.last_name, email=user.email)
            user.set_password(user.password)
            user.save()
            return redirect("/")
        else:
            page_data = {"join_form": join_form}
            return render(request, 'Core/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = {"join_form": join_form}
        return render(request, 'Core/join.html', page_data)
def user_login(request):
    context = {"messages": "", "login_form": LoginForm}
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    try:
                        UserProfile.objects.get(user=user)
                    except:
                        UserProfile.objects.create(
                            user=user, first_name=user.first_name, last_name=user.last_name, email=user.email)
                    login(request, user)
                    return redirect("/")
                else:
                    return HttpResponse("Your account is not active.")
            else:
                context["messages"] = "Invalid username or password"
                return render(request, 'Core/login.html', context)
    else:
        return render(request, 'Core/login.html', context)
@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect("/")
def settings(request):
    try:
        user = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user = UserProfile.objects.create(
            user=request.user, first_name=request.user.first_name, last_name=request.user.last_name, email=request.user.email)
    form = EditSettings(instance=user)
    if request.method == 'POST' and 'update' in request.POST:
        form = EditSettings(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
    context = {'form': form}
    return render(request, 'Core/settings.html', context)
