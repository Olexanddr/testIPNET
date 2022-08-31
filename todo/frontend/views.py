from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "frontend/main.html")

def login(request):
    return render(request, "frontend/login.html")

def register(request):
    return render(request, "frontend/register.html")