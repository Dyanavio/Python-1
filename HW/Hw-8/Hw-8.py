from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<button style="background-color:lightblue; border-radius:5px; color:white">Main page 2</button>')

def date(request):
    import datetime
    date = datetime.datetime.now()
    return HttpResponse(f"<h1>Now is {date.hour}:{date.minute}:{date.second}, {date.day}.{date.month}.{date.year}</h1>")

def multiplicationTable(request):
    table = "<table><tbody>"
    table += '<tr style="background-color: lightgray"><th> </th>'
    for i in range(1, 11):
        table += f"<th>{i}</th>"
    table += "</tr>"

    for i in range(1, 11):
        table += f'<tr><th style="background-color: lightgray">{i}</th>'
        for j in range(1, 11):
            table += f"<td>{i * j}</td>"
        table += "</tr>"
    table += "</tbody></table>"
    return HttpResponse(table)

def programmersDay(request):
    from datetime import datetime, timedelta
    firstDay = datetime(datetime.now().year, 1, 1)
    programmersDayDate = firstDay + timedelta(days=255)

    return HttpResponse(programmersDayDate)