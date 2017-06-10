from django.conf.urls import url
from . import views
app_name = "main"

urlpatterns = [

    url(r'^$',views.main, name = "main"),
    url(r'^home/$',views.home, name = "home"),

    url(r'^calendar/$',views.event, name = "event"),
    url(r'^createEvent/$',views.createEvent, name = "createEvent"),
    url(r'^editEvent/(?P<events_id>[0-9]+)$',views.editEvent, name = "editEvent"),
    url(r'^deleteEvent/(?P<events_id>[0-9]+)$',views.deleteEvent, name = "deleteEvent"),
    url(r'^event/$',views.event_page, name = "event_page"),

    url(r'^ad/$',views.admin_page, name = "admin_page"),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^logout/$',views.logout, name = "logout"),
    url(r'^naughty_page/$',views.naughty_page, name = "naughty_page"),
    url(r'^user_list/$',views.user_list, name = "user_list"),
    url(r'^user_coffees/(?P<user_id>[0-9]+)$',views.user_coffees, name = "user_coffees"),

    url(r'^send_order_email/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$',views.send_order_email, name = "send_order_email"),
    url(r'^replecate_order/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$',views.replecate_order, name = "replecate_order"),
    url(r'^received_order/(?P<order_id>[0-9]+)/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$',views.received_order, name = "received_order"),
    url(r'^sent/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$',views.sent, name = "sent"),
    url(r'^createCoffee/$',views.createCoffee, name = "createCoffee"),
    url(r'^editCoffee/(?P<coffee_id>[0-9]+)$',views.editCoffee, name = "editCoffee"),
    url(r'^deleteCoffee/(?P<coffee_id>[0-9]+)$',views.deleteCoffee, name = "deleteCoffee"),
    url(r'^createBean/$',views.createBean, name = "createBean"),
    url(r'^editBean/(?P<bean_id>[0-9]+)$',views.editBean, name = "editBean"),
    url(r'^deleteBean/(?P<bean_id>[0-9]+)$',views.deleteBean, name = "deleteBean"),
    url(r'^createRoast/$',views.createRoast, name = "createRoast"),
    url(r'^editRoast/(?P<roast_id>[0-9]+)$',views.editRoast, name = "editRoast"),
    url(r'^deleteRoast/(?P<roast_id>[0-9]+)$',views.deleteRoast, name = "deleteRoast"),
    url(r'^createSyrup/$',views.createSyrup, name = "createSyrup"),
    url(r'^editSyrup/(?P<syrup_id>[0-9]+)$',views.editSyrup, name = "editSyrup"),
    url(r'^deleteSyrup/(?P<syrup_id>[0-9]+)$',views.deleteSyrup, name = "deleteSyrup"),
    url(r'^createPowder/$',views.createPowder, name = "createPowder"),
    url(r'^editPowder/(?P<powder_id>[0-9]+)$',views.editPowder, name = "editPowder"),
    url(r'^deletePowder/(?P<powder_id>[0-9]+)$',views.deletePowder, name = "deletePowder"),
    url(r'^createOrder/(?P<coffee_id>[0-9]+)$',views.createOrder, name = "createOrder"),

]
