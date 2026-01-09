from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from main.forms import *
from main.models import *
from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    context = {"title": "All Offers", "restaurants": Restaurant.objects.all()}
    return render(request, "index.html", context=context)


def create(request):
    if(request.method == "POST"):
        form = RestaurantForm(request.POST)
        if form.is_valid():
            Restaurant.objects.create(**form.cleaned_data)
            return redirect(reverse("main"))
        else:
            context = {"title": "Restaurant Creation", "form": form}
    else:
        form = RestaurantForm()
        context = {"title": "Restaurant Creation", "form": form}
    return render(request, "create.html", context=context)

@csrf_protect
def search(request):
    if(request.method == "POST"):
        form = SearchForm(request.POST)
        if(form.is_valid()):
            requestedSpecialization = form.cleaned_data["specialization"]
            if(requestedSpecialization):
                restaurants = Restaurant.objects.filter(specialization = requestedSpecialization).values()
                context = {
                    "title": "Search",
                    "form": SearchForm(),
                    "restaurants": restaurants
                }
                return render(request, "search.html", context=context)
            else:
                context = { "title": "Search", "form": SearchForm() }
                return render(request, "search.html", context=context)
    else:
        context = {"title": "Search", "form": SearchForm()}
        return render(request, "search.html", context=context)


def manage(request, id:int):
    if(request.method == "POST"):
        restaurant = Restaurant.objects.filter(pk = id).first()
        form = RestaurantForm(request.POST, instance=restaurant)
        if(form.is_valid()):
            form.save()
        return redirect(reverse("main"))
    else:
        restaurant = Restaurant.objects.filter(pk = id).first()
        if(restaurant):
            form = RestaurantForm(instance=restaurant)
            context = {
                "title": "Manage Restaurant",
                "form": form,
                "restaurant": restaurant
            }
            return render(request, "manage.html", context=context)
        else:
            context = {
                "title": "No restaurant was found"
            }
            return render(request,"manage.html", context=context)


def delete(request, id:int):
    restaurant = Restaurant.objects.filter(pk = id).first()
    if(restaurant):
        restaurant.delete()
    return redirect(reverse("main"))
   