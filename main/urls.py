from django.conf.urls import url
from . import views
app_name = "main"

urlpatterns = [

    url(r'^$',views.main),
    url(r'^home/$',views.home, name = "home"),
    url(r'^user_list/$',views.user_list, name = "user_list"),
    url(r'^user_coffees/(?P<user_id>[0-9])$',views.user_coffees, name = "user_coffees"),

    url(r'^send_order_email/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$',views.send_order_email, name = "send_order_email"),

    url(r'^createCoffee/$',views.createCoffee, name = "createCoffee"),
    url(r'^editCoffee/(?P<coffee_id>[0-9])$',views.editCoffee, name = "editCoffee"),
    url(r'^deleteCoffee/(?P<coffee_id>[0-9])$',views.deleteCoffee, name = "deleteCoffee"),
    url(r'^createBean/$',views.createBean, name = "createBean"),
    url(r'^editBean/(?P<bean_id>[0-9])$',views.editBean, name = "editBean"),
    url(r'^createRoast/$',views.createRoast, name = "createRoast"),
    url(r'^editRoast/(?P<roast_id>[0-9])$',views.editRoast, name = "editRoast"),
    url(r'^createSyrup/$',views.createSyrup, name = "createSyrup"),
    url(r'^editSyrup/(?P<syrup_id>[0-9])$',views.editSyrup, name = "editSyrup"),
    url(r'^createPowder/$',views.createPowder, name = "createPowder"),
    url(r'^editPowder/(?P<powder_id>[0-9])$',views.editPowder, name = "editPowder"),
    url(r'^createOrder/(?P<coffee_id>[0-9])$',views.createOrder, name = "createOrder"),

]
