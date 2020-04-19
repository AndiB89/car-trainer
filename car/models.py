from django.db import models
from django.db.models.aggregates import Count
import random
from random import randint

# Create your models here.
class CarManager(models.Manager):
    def random(self, amount, maxNumber):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        random_list = random.sample(range(1, maxNumber+1), amount)
        print(random_list)
        return self.filter(pk__in = random_list)#self.all()[amount]


class Car(models.Model):
    objects = CarManager()
    name = models.CharField(max_length=128)
    series = models.CharField(max_length=256, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    releaseYear = models.IntegerField(blank=True, null=True)
    isStillProduced = models.BooleanField(blank=True, null=True)
    picName = models.CharField(max_length=256)
    images = models.ImageField(upload_to="img",null=True, blank=True)
    #category = models.ManyToManyField(Category, blank=True, null=True, related_name="relevantLocations")

    def __str__(self):
        return f"{self.id} - {self.name} ({self.series} - {self.releaseYear})"

