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

]
