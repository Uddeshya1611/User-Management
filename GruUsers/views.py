from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.utils import timezone
from .models import Gruser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .forms import Signup, Login

# Create your views here.
def home(request):
    return render(request, 'GruUsers/home.html', {})

def about(request):
	username = 'uddeshya'
	text = 'T'
	context = {
		'username': username,
		'else': text
	}
	return render(request, 'GruUsers/about.html', context)

def user_detail(request):
	return render(request, 'GruUsers/userdetail.html', {})

def account_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		if username and password:
			user = Gruser.objects.get(username__exact=username)
		if user is not None and user.password==password:
			user = authenticate(request, username=username, password=password)
			login(request, user)
			return render(request, 'GruUsers/userdetail.html', {})
	form = Login()
	return render(request, 'GruUsers/signin.html', {'form':form})

def account_logout(request):
	logout(request)
	return render(request, 'GruUsers/about.html', {})

def account_signup(request):
	if request.method == "POST":
		form = Signup(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.password = request.POST['password']
			user.join_date = timezone.now()
			user.save()
			return redirect('account_login')
	else:
		form = Signup()
	return render(request, 'GruUsers/register.html', {'form':form})