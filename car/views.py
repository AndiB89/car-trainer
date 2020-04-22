from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
import json 
from .models import Car
from django.core.exceptions import ObjectDoesNotExist

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

    correctAnswer = 0
    listAnswer = []
    dictResults = {}
    try:
        listIds=request.POST['list']
        listIds=json.loads(listIds)

        for key, value in request.POST.items():
            if key != "list" and key != "csrfmiddlewaretoken":
                listAnswer.append(value)
                print("Test KEy Value")
                print(key, value)   


        for i in range(len(listIds)):
            print("ANALYSE")
            print("Test i: " + str(listIds[i]))
            try:
                carCorrect=Car.objects.get(pk=listIds[i])
                print(listAnswer[i])
                carAnswer = Car.objects.get(series=listAnswer[i])
            except ObjectDoesNotExist:
                print("Object not exists")

            result = {}
            result["answer"] = listAnswer[i]
            result["correct"] = carCorrect.series
            result["result"] = True if carCorrect == carAnswer else False
            dictResults[i] = result


            if carCorrect == carAnswer:
                correctAnswer +=1
                print("YEEEEAH")
            #print(car)
        print("Anzahl richtiger Antworten: ")
        print(correctAnswer)
        print("Finale Tabelle")
        print(dictResults)
    except:
        raise ValueError("Something went wrong.")
    print("Post Fkt")

    return redirect('index')