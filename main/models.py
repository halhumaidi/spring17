from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bean(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Roast(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Syrup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Powder(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Coffee(models.Model):
    user= models.ForeignKey(User)
    name = models.CharField(max_length = 255)
    bean = models.ForeignKey(Bean)
    roast = models.ForeignKey(Roast)
    esspreso_shots = models.PositiveIntegerField(default = 1)
    water = models.FloatField(default = 0)
    steamed_milk = models.BooleanField(default = False)
    foam = models.FloatField(default = 0)
    powder = models.ManyToManyField(Powder, blank=True)
    syrup = models.ManyToManyField(Syrup, blank=True)
    extra_instructions = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User)
    coffee = models.ForeignKey(Coffee)
    date = models.DateField()

    def __str__(self):
        return str(self.user)

class Events(models.Model):
    event_name = models.CharField(max_length=255,null=True,blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    event_type = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.event_name
