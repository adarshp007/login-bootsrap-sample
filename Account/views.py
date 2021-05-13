from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'nav.html')
def signup(request):
    return render(request,'signup.html')
def login(request):
    return render(request,'login.html')