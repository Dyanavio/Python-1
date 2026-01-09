from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.views.generic import TemplateView
from main.forms import *
from django.core.files.storage import FileSystemStorage

def index(request):
    pass


@csrf_protect
def getContacts1(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, "contacts1.html", {"sent": True})
    else:
        form = ContactForm()
    return render(request, "contacts1.html", context={"form": form})


@csrf_protect
def getContacts(request):
    form = {}
    if(request.method == "POST"):
        form["name"]      = request.POST.get('name')
        form["age"]       = request.POST.get('age')
        form["email"]     = request.POST.get('email')
        form["biography"] = request.POST.get('biography')
        form["agreement"] = request.POST.get('agreement')
        
        #Validation

        form['sent'] = True
        return render(request, 'contacts.html', context=form)
    return render(request, 'contacts.html', context={ "sent": False })


#----------------------------------------------------------------------------


@csrf_protect
def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            return render(request, "review.html", context={"sent": True})
    else:
        form = ReviewForm()
    return render(request, "review.html", context={"form": form})


@csrf_protect
def addFilm(request):
    if request.method == "POST":
        form = AddFilmForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES:
                poster = request.FILES['poster']
                fileSystemStorage = FileSystemStorage()
                fileSystemStorage.save(poster.name, poster)
            return render(request, "films.html", {"sent": True})
    else:
        form = AddFilmForm()
    return render(request, "films.html", context={"form": form, "sent": False})