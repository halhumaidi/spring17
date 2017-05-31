from django.conf.urls import url
from . import views
app_name = "main"

urlpatterns = [

    url(r'^$',views.main),
    url(r'^home/$',views.home, name = "home"),
    url(r'^createCoffee/$',views.createCoffee, name = "createCoffee"),
    url(r'^editCoffee/(?P<coffee_id>[0-9])$',views.editCoffee, name = "editCoffee"),
    url(r'^createBean/$',views.createBean, name = "createBean"),
    url(r'^editBean/(?P<bean_id>[0-9])$',views.editBean, name = "editBean"),
    url(r'^createRoast/$',views.createRoast, name = "createRoast"),
    url(r'^editRoast/(?P<roast_id>[0-9])$',views.editRoast, name = "editRoast"),
    url(r'^createSyrup/$',views.createSyrup, name = "createSyrup"),
    url(r'^editSyrup/(?P<syrup_id>[0-9])$',views.editSyrup, name = "editSyrup"),
    url(r'^createPowder/$',views.createPowder, name = "createPowder"),
    url(r'^editPowder/(?P<powder_id>[0-9])$',views.editPowder, name = "editPowder"),

]
