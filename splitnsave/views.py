from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html')

def signup(request):
	return render(request,'signup.html')

def editprofile(request):
	return render(request,'edit_profile.html')