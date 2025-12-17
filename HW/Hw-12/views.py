from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core.serializers.json import DjangoJSONEncoder
from django.views import View


def index(request):
    return render(request, "index.html")

def silksong(request):
    return render(request, "silksong.html")

def silksongGlobal(request, language):
    text = []
    if(language == "fr"):
        text = ["Ils voient ta beauté, si fragile et si délicate,",
                "Ils voient votre paix, tissée de foi et de labeur,",
                "Ils oublient ton cœur, prisonnier du sommeil et de la servitude,",
                "Quand tu te réveilleras, ils verront ta vérité.",
                "La nature d'une bête mise à nu à tous.",
                "- Extrait de «La Folie de Phrloom» du chef d'orchestre Romino"]
    elif(language == "de"):
        text = ["Sie sehen deine Schönheit, so zart und fein.",
                "Sie sehen deinen Frieden, gewoben aus Glauben und Mühe.",
                "Sie vergessen dein Herz, gefangen in Schlummer und Knechtschaft.",
                "Wenn du erwachst, werden sie deine Wahrheit erkennen.",
                "Das wahre Wesen eines Tieres wird allen offenbart.",
                "- Aus «Pharlooms Folly» von Dirigent Romino"]
    elif(language == "ru"):
         text = ["Зрят они твою красоту, коя столь хрупка и нежна,",
                "Твой покой, из веры и труда сплетенный,",
                "Но про сердце твое, в оковах сна и рабства забывают.",
                "Когда же пробудишься, познают они истину твою,",
                "И звериный дух твой откроется всякому",
                "- Отрывок из «Фарлумского сумасбродства» проводника Ромино"]
    else:
        return HttpResponseRedirect("/silksong/")
    return render(request, "silksongGlobal.html", context={"text": text})

def cars(request):
    return render(request, "carsMain.html")

def carMark(request, mark: str):
    mark = mark.capitalize()
    source = f"https://placehold.co/600x400?font=roboto&text=Pretend+there+is+{mark}+image"
    return render(request, "carMark.html", context={"mark": mark, "source": source})

def weekday(request, weekday):
    from datetime import date
    #weekday = date.today().weekday()
    weekday -= 1
    day = ""
    colour = ""
    match weekday:
        case 0:
            day = "Monday"
            colour = "lightblue"
        case 1:
            day = "Tuesday"
            colour = "lightgray"
        case 2:
            day = "Wednesday"
            colour = "lightcoral"
        case 3:
            day = "Thursday"
            colour = "lightyellow"
        case 4:
            day = "Friday"
            colour = "lightseagreen"
        case 5:
            day = "Saturday"
            colour = "lightgreen"
        case 6:
            day = "Sunday"
            colour = "lightslategrey"
    return render(request, "weekday.html", context={"day": day, "colour": colour})

def headphones(request):
    model = request.GET.get('model')
    return render(request, "headphones.html", context={"model": model})