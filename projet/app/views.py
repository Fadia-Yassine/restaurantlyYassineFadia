from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'app/index.html')

def base(request):
    return render(request,'base.html')

def about(request):
    return render(request, 'aboutUs.html')

def menu(request):
    return render(request, 'menu.html')

def special(request):
    return render(request, 'special.html')

def events(request):
    return render(request, 'events.html')

def chefs(request):
    return render(request, 'chefs.html')

def gallery(request):
    return render(request, 'gallery.html')

def chefsSection(request):
    return render(request, 'chefsSection.html')

def contact(request):
    return render(request, 'contact.html')