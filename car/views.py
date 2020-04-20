from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
import json 
from .models import Car

# Create your views here.
def index(request):
    context = {
        "maxRounds" : len(Car.objects.all())
    }
    
    return render(request, "car/index.html", context)


@require_POST
def game(request):
    amount=int(request.POST['n_rounds'])
    cars,listIds = Car.objects.random(amount=amount, maxNumber=len(Car.objects.all()))
    print(cars)
    print(listIds)

    context = {
        "cars": cars,
        "list": listIds,
    }

    return render(request, "car/game.html", context)


@require_POST
def checkSeries(request):
    # form = TodoForm(request.POST)
    # if form.is_valid():
    #     new_todo = Todo(text=request.POST['text'])
    #     new_todo.save()
    print("Post Fkt")

    try:
        listIds=request.POST['list']
        listIds=json.loads(listIds)

        for key, value in request.POST.items():
            print(key, value)   

        print(len(listIds))
    except:
        raise ValueError("Something went wrong.")
    print("Post Fkt")

    return redirect('index')