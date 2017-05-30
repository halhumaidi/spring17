from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *

def main(request):

    context = {}

    return render(request, "main/homepage.html", context)

def home(request):
    return render(request, "main/home.html", {})


def createCoffee(request):
    context = {}
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        context["form"]=form
        if form.is_valid():
            coffee = form.save(commit=False)
            coffee.user = request.user
            coffee.save()
            form.save_m2m()
            return redirect("main:home")
        else:
            return render(request, "main/createCoffee.html", context)
    else:
        form = CoffeeForm()
        context["form"]=form
        return render(request, "main/createCoffee.html", context)

def editCoffee(request, coffee_id):
    context = {}
    coffee = Coffee.objects.get(id=coffee_id)
    context["coffee"]=coffee

    if request.method == "POST":
        form = CoffeeForm(request.POST, instance=coffee)
        context["form"]=form
        if form.is_valid():
            coffee = form.save(commit=False)
            coffee.user = request.user
            coffee.save()
            form.save_m2m()
            return redirect("main:home")
        else:
            return render(request, "main/editCoffee.html", context)
    else:
        form = CoffeeForm(instance=coffee)
        context["form"]=form
        return render(request, "main/editCoffee.html", context)
