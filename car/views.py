from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Car

# Create your views here.
def index(request):
    context = {
        "maxRounds" : len(Car.objects.all())
    }
    
    return render(request, "car/index.html", context)

@require_POST
def checkSeries(request):
    # form = TodoForm(request.POST)
    # if form.is_valid():
    #     new_todo = Todo(text=request.POST['text'])
    #     new_todo.save()

    # try:
    #     loc = Location(name=request.POST['n_location'], url=request.POST['n_url'], visited = 'n_isvisited' in request.POST, pricing = request.POST['n_pricing'] )
    #     if not Location.objects.filter(name = loc.name).exists():
    #         loc.save()
    # except:
    #     raise ValueError("Something went wrong.")
    print("Post Fkt")

    return redirect('index')

@require_POST
def game(request):
    amount=int(request.POST['n_rounds'])
    cars = Car.objects.random(amount=amount, maxNumber=len(Car.objects.all()))
    print(cars)
    context = {
        "cars": cars,
    }

    return render(request, "car/game.html", context)
