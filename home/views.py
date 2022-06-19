import email
from django.shortcuts import render, redirect , HttpResponse
from home.models import details
# Create your views here.
def index(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        detail = details(name=name,email=email)
        detail.save()
    return render(request,'index.html')