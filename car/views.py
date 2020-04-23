from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
import json 
from .models import Car
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):

    modi = []
    modi.append("Klassenbezeichnung")
    modi.append("Baureihe")
    context = {
        "maxRounds" : len(Car.objects.all()),
        "modi" : modi
    }

    print("Max Anzahl an Autos: " + str(len(Car.objects.all())))
    print("Mögliche Spielmodi: " + str(modi))

    
    return render(request, "car/index.html", context)


@require_POST
def game(request):
    amount=int(request.POST['n_rounds'])
    modus=request.POST['modus']

    print("Max gewünschter Runden: " + str(amount))
    print("Modus: " + str(modus))

    cars,listIds = Car.objects.random(amount=amount, maxNumber=len(Car.objects.all()))
    print("Liste an Autos: " + str(cars))
    print("Liste der Random Ids" + str(listIds))

    context = {
        "cars": cars,
        "list": listIds,
        "modus": modus,
    }

    return render(request, "car/game.html", context)


@require_POST
def result(request):
    # form = TodoForm(request.POST)
    # if form.is_valid():
    #     new_todo = Todo(text=request.POST['text'])
    #     new_todo.save()

    correctAnswer = 0
    listAnswer = []
    listResults = []
    carAnswer=""
    try:
        modus=request.POST['modus']
        listIds=request.POST['list']
        listIds=json.loads(listIds)

        for key, value in request.POST.items():
            # only answers, therefore filter config values
            if key != "list" and key != "modus" and key != "csrfmiddlewaretoken":
                listAnswer.append(value)
                print("Antworten:")
                print(key, value)   

        print("Liste an Autos: " + str(listIds))
        for i in range(len(listIds)):
            print("Runde: " + str(i))
            print("Auto: " + str(listIds[i]))
            try:
                carCorrect=Car.objects.get(pk=listIds[i])
                #print(listAnswer[i])
                if modus == "Klassenbezeichnung":
                    #Queryset with multiple values
                    carAnswer = Car.objects.filter(class_name=listAnswer[i])
                    print("Auto: "+ str(carAnswer))
                elif modus == "Baureihe":
                    #Series is unique > one value in carAnswer
                    carAnswer = Car.objects.get(series=listAnswer[i])

            except ObjectDoesNotExist:
                print("Object not exists")

            result = {}
            result["answer"] = listAnswer[i]
            result["correct"] = carCorrect.series
            result["name"] = carCorrect.name
            result["image"] = carCorrect.images

            if modus == "Klassenbezeichnung":
                #print("Klassenbezeichnung")
                result["result"] = "Leider falsch"
                for answer in carAnswer:
                    if carCorrect == answer:
                        correctAnswer +=1
                        result["result"] = "Korrekt" 
                        break                        

            elif modus == "Baureihe": 
                if carCorrect == carAnswer:
                    correctAnswer +=1
                result["result"] = "Korrekt" if carCorrect == carAnswer else "Leider falsch"

            listResults.append(result)

            
        print("Anzahl richtiger Antworten: ")
        print(correctAnswer)

        context = { 
            "results" : listResults,
            "correctAnswer" : correctAnswer,
            "rounds" : len(listResults),
            "maxRounds" : len(Car.objects.all()),
            "modus" : modus,
        }
        print(context)
    except:
        raise ValueError("Something went wrong.")

    return render(request, "car/result.html", context)
    #return redirect('index')