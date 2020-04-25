from django.db import models
from django.db.models import Case, When
from django.db.models.aggregates import Count
import random
from random import randint

# Create your models here.
class CarManager(models.Manager):
    def random(self, amount, maxNumber):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        random_list = random.sample(range(1, maxNumber+1), amount)
        #print(random_list)

        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(random_list)])
        queryset = self.filter(pk__in=random_list).order_by(preserved)   
        return queryset, random_list
        # self.filter(pk__in = random_list), random_list


class Car(models.Model):
    objects = CarManager()
    name = models.CharField(max_length=128)
    class_name = models.CharField(max_length=128, default="")
    series = models.CharField(max_length=256, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    releaseYear = models.IntegerField(blank=True, null=True)
    isStillProduced = models.BooleanField(blank=True, null=True)
    image = models.ImageField(upload_to="img",null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.name} ({self.series} - {self.releaseYear} - {self.image})"

class Game(models.Model):
    givenanswer = models.CharField(max_length=256, blank=True, null=True)
    correctCar = models.ForeignKey(Car, on_delete=models.CASCADE, default="")
    correct = models.BooleanField(blank=True, null=True)
    rownumber = models.IntegerField(blank=True, null=True)
    sessionid = models.CharField(max_length=256, blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    modus = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.givenanswer} - {self.correctCar} - {self.correct} - {self.rownumber} - {self.creation_date} - {self.sessionid}"