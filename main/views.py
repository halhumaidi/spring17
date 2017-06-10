from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import logout as django_logout



def naughty_page(request):
    return render(request, 'main/naughty_page.html', {})

def home(request):
    context = {}
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
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

def logout(request):
    django_logout(request)
    return redirect("main:main")

def main(request):

    context = {}

    return render(request, "main/index.html", context)




def createCoffee(request):
    context = {}
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
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
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
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
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
    Coffee.objects.get(id=coffee_id).delete()
    return redirect("main:home")

def createBean(request):
    context={}
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    if request.method == "POST":
        form = BeanForm(request.POST)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:admin_page")
        else:
            return render(request, "main/createBean.html", context)
    else:
        form = BeanForm()
        context["form"]=form
        return render(request, "main/createBean.html", context)

def editBean(request, bean_id):
    context = {}
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    bean = Bean.objects.get(id=bean_id)
    context["bean"]=bean

    if request.method == "POST":
        form = BeanForm(request.POST, instance=bean)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:admin_page")
        else:
            return render(request, "main/editBean.html", context)
    else:
        form = BeanForm(instance=bean)
        context["form"]=form
        return render(request, "main/editBean.html", context)

def deleteBean(request, bean_id):
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    Bean.objects.get(id=bean_id).delete()
    return redirect("main:admin_page")

def createRoast(request):
    context={}
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    if request.method == "POST":
        form = RoastForm(request.POST)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:admin_page")
        else:
            return render(request, "main/createRoast.html", context)
    else:
        form = RoastForm()
        context["form"]=form
        return render(request, "main/createRoast.html", context)

def editRoast(request, roast_id):
    context = {}
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    roast = Roast.objects.get(id=roast_id)
    context["roast"]=roast

    if request.method == "POST":
        form = RoastForm(request.POST, instance=roast)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:admin_page")
        else:
            return render(request, "main/editRoast.html", context)
    else:
        form = RoastForm(instance=roast)
        context["form"]=form
        return render(request, "main/editRoast.html", context)

def deleteRoast(request, roast_id):
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    Roast.objects.get(id=roast_id).delete()
    return redirect("main:admin_page")

def createSyrup(request):
    context={}
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    if request.method == "POST":
        form = SyrupForm(request.POST)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:admin_page")
        else:
            return render(request, "main/createSyrup.html", context)
    else:
        form = SyrupForm()
        context["form"]=form
        return render(request, "main/createSyrup.html", context)

def editSyrup(request, syrup_id):
    context = {}
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    syrup = Syrup.objects.get(id=syrup_id)
    context["syrup"]=syrup

    if request.method == "POST":
        form = SyrupForm(request.POST, instance=syrup)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:admin_page")
        else:
            return render(request, "main/editSyrup.html", context)
    else:
        form = SyrupForm(instance=syrup)
        context["form"]=form
        return render(request, "main/editSyrup.html", context)

def deleteSyrup(request, syrup_id):
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    Syrup.objects.get(id=syrup_id).delete()
    return redirect("main:admin_page")

def createPowder(request):
    context={}
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    if request.method == "POST":
        form = PowderForm(request.POST)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:admin_page")
        else:
            return render(request, "main/createPowder.html", context)
    else:
        form = PowderForm()
        context["form"]=form
        return render(request, "main/createPowder.html", context)

def editPowder(request, powder_id):
    context = {}
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    powder = Powder.objects.get(id=powder_id)
    context["powder"]=powder

    if request.method == "POST":
        form = PowderForm(request.POST, instance=powder)
        context["form"]=form
        if form.is_valid():
            form.save()
            return redirect("main:admin_page")
        else:
            return render(request, "main/editPowder.html", context)
    else:
        form = PowderForm(instance=powder)
        context["form"]=form
        return render(request, "main/editPowder.html", context)

def deletePowder(request, powder_id):
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    Powder.objects.get(id=powder_id).delete()
    return redirect("main:admin_page")


def createOrder(request, coffee_id):
    context={}
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
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
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    user_list = User.objects.all()
    context['user_list'] = user_list
    return render(request, 'main/user_list.html', context)

def user_coffees(request, user_id):
    context = {}
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    user = User.objects.get(id=user_id)
    context['user']=user
    coffees = Coffee.objects.filter(user=user)
    context['coffees']=coffees
    return render(request, 'main/user_coffees.html', context)



def send_order_email(request, year, month, day):
    context = {}
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
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

def replecate_order(request, year, month, day):
    context = {}
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
    date = datetime.datetime.strptime('%s%s%s'%(year, month, day), '%Y%m%d').date()
    context['today'] = date
    order_list = Order.objects.filter(user=request.user, date=date)

    if request.method =="POST":
        form = SearchForm(request.POST)
        context['form'] = form
        if form.is_valid():
            obj = form.cleaned_data['date']
            for order in order_list:
                new_order = Order(user=order.user, coffee=order.coffee, date=obj)
                new_order.save()
            return redirect("main:home")

        else:
            return render(request, "main/replecate_order.html", context)

    else:
        form = SearchForm()
        context['form'] = form

    return render(request, "main/replecate_order.html", context)

def received_order(request, year, month, day):
    context = {}
    date = datetime.datetime.strptime('%s%s%s'%(year, month, day), '%Y%m%d').date()
    context['today'] = date
    if not request.user.is_authenticated():
        return redirect('/accounts/github/login')
    Order.objects.get(date=date).delete()
    return redirect("main:home")

def sent(request, year, month, day):
    context = {}
    date = datetime.datetime.strptime('%s%s%s'%(year, month, day), '%Y%m%d').date()
    context['today'] = date
    Order.objects.get(date=date).delete()
    return redirect("main:admin_page")

def event(request):
    all_events = Events.objects.all()
    get_event_types = Events.objects.only('event_type')

    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:
        event_arr = []
        if request.GET.get('event_type') == "all":
            all_events = Events.objects.all()
        else:
            all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_type'))

        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.event_name
            start_date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events":all_events,
        "get_event_types":get_event_types,

    }
    return render(request,'main/homepage.html', context)

def admin_page(request):
    context={}
    if not request.user.is_authenticated():
      return redirect('/admin')
    if not request.user.is_staff:
      return redirect("main:naughty_page")
    form = SearchForm()
    context["form"]=form
    today = datetime.date.today()
    context['today']=today
    order_list = Order.objects.filter(date=today)
    context['order_list']=order_list
    coffee_list = Coffee.objects.all()
    context['coffee_list']=coffee_list
    bean = Bean.objects.all()
    context['bean']=bean
    roast = Roast.objects.all()
    context['roast']=roast
    powder = Powder.objects.all()
    context['powder']=powder
    syrup = Syrup.objects.all()
    context['syrup']=syrup

    return render(request,'main/admin_page.html',context)
