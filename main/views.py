from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
import datetime
from django.core.mail import send_mail
from django.conf import settings

def main(request):

    context = {}

    return render(request, "main/homepage.html", context)




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

def deleteCoffee(request, coffee_id):
    Coffee.objects.get(id=coffee_id).delete()
    return redirect("main:home")

def createBean(request):
    context={}
    if request.method == "POST":
        form = BeanForm(request.POST)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:home")
        else:
            return render(request, "main/createBean.html", context)
    else:
        form = BeanForm()
        context["form"]=form
        return render(request, "main/createBean.html", context)

def editBean(request, bean_id):
    context = {}
    bean = Bean.objects.get(id=bean_id)
    context["bean"]=bean

    if request.method == "POST":
        form = BeanForm(request.POST, instance=bean)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:home")
        else:
            return render(request, "main/editBean.html", context)
    else:
        form = BeanForm(instance=bean)
        context["form"]=form
        return render(request, "main/editBean.html", context)

def deleteBean(request, bean_id):
    Bean.objects.get(id=bean_id).delete()
    return redirect("main:home")

def createRoast(request):
    context={}
    if request.method == "POST":
        form = RoastForm(request.POST)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:home")
        else:
            return render(request, "main/createRoast.html", context)
    else:
        form = RoastForm()
        context["form"]=form
        return render(request, "main/createRoast.html", context)

def editRoast(request, roast_id):
    context = {}
    roast = Roast.objects.get(id=roast_id)
    context["roast"]=roast

    if request.method == "POST":
        form = RoastForm(request.POST, instance=roast)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:home")
        else:
            return render(request, "main/editRoast.html", context)
    else:
        form = RoastForm(instance=roast)
        context["form"]=form
        return render(request, "main/editRoast.html", context)

def deleteRoast(request, roast_id):
    Roast.objects.get(id=roast_id).delete()
    return redirect("main:home")

def createSyrup(request):
    context={}
    if request.method == "POST":
        form = SyrupForm(request.POST)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:home")
        else:
            return render(request, "main/createSyrup.html", context)
    else:
        form = SyrupForm()
        context["form"]=form
        return render(request, "main/createSyrup.html", context)

def editSyrup(request, syrup_id):
    context = {}
    syrup = Syrup.objects.get(id=syrup_id)
    context["syrup"]=syrup

    if request.method == "POST":
        form = SyrupForm(request.POST, instance=syrup)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:home")
        else:
            return render(request, "main/editSyrup.html", context)
    else:
        form = SyrupForm(instance=syrup)
        context["form"]=form
        return render(request, "main/editSyrup.html", context)

def deleteSyrup(request, syrup_id):
    Syrup.objects.get(id=syrup_id).delete()
    return redirect("main:home")

def createPowder(request):
    context={}
    if request.method == "POST":
        form = PowderForm(request.POST)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:home")
        else:
            return render(request, "main/createPowder.html", context)
    else:
        form = PowderForm()
        context["form"]=form
        return render(request, "main/createPowder.html", context)

def editPowder(request, powder_id):
    context = {}
    powder = Powder.objects.get(id=powder_id)
    context["powder"]=powder

    if request.method == "POST":
        form = PowderForm(request.POST, instance=powder)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:home")
        else:
            return render(request, "main/editPowder.html", context)
    else:
        form = PowderForm(instance=powder)
        context["form"]=form
        return render(request, "main/editPowder.html", context)

def deletePowder(request, powder_id):
    Powder.objects.get(id=powder_id).delete()
    return redirect("main:home")


def createOrder(request, coffee_id):
    context={}
    coffee = Coffee.objects.get(id=coffee_id)
    context['coffee']=coffee
    if request.method == "POST":
        form = OrderForm(request.POST)
        context['form']=form
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.coffee = coffee
            order.save()
            return redirect("main:home")
        else:
            return render(request, 'main/createOrder.html', context)
    else:
        form = OrderForm()
        context['form']=form
        return render(request, 'main/createOrder.html', context)

def user_list(request):
    context = {}
    user_list = User.objects.all()
    context['user_list'] = user_list
    return render(request, 'main/user_list.html', context)

def user_coffees(request, user_id):
    context = {}
    user = User.objects.get(id=user_id)
    context['user']=user
    coffees = Coffee.objects.filter(user=user)
    context['coffees']=coffees
    return render(request, 'main/user_coffees.html', context)

def home(request):
    context = {}
    user = request.user
    context['user']=user
    if request.method=="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            context['form']=form
            date = form.cleaned_data['date']
            context['today']=date
            order_list = Order.objects.filter(user=user, date=date)
            context["order_list"]=order_list
    else:
        form = SearchForm()
        context["form"]=form
        today = datetime.date.today()
        context['today']=today
        order_list = Order.objects.filter(user=user, date=today)
        context['order_list']=order_list
    coffee_list = Coffee.objects.filter(user=user)
    context['coffee_list']=coffee_list
    return render(request, "main/home.html", context)

def send_order_email(request, year, month, day):
    context = {}
    date = datetime.datetime.strptime('%s%s%s'%(year, month, day), '%Y%m%d').date()
    order_list = Order.objects.filter(user=request.user, date=date)
    subject = "HAHAAAA SPAAM I OWN YOUUUU!!! YOU ARE A NOOB!!"
    subject2 = "Coded coffee request!"
    message = "These are my orders, make yourself useful and get them:\n"
    for order in order_list:
        message += "%s,"%(order.coffee)

    message2 = "Today`s orders:\n"
    for order in order_list:
        message2 += "%s,"%(order.coffee)

    send_mail(subject, message, settings.EMAIL_HOST_USER, ['alsaff1987@gmail.com', 'haya.b.alhumaidi@gmail.com',])
    send_mail(subject2, message2, settings.EMAIL_HOST_USER, ['hashim@joincoded.com', 'haya.b.alhumaidi@gmail.com',])
    return redirect("main:home")
