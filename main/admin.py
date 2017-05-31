from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Bean)
admin.site.register(Roast)
admin.site.register(Syrup)
admin.site.register(Powder)
admin.site.register(Coffee)
admin.site.register(Order)
