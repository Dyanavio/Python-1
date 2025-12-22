from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.views.generic import TemplateView
import statistics, calendar
import datetime

def index(request):
    return HttpResponse()


class User:
    def __init__(self, userlogin, password, role):
        self.userlogin = userlogin
        self.password = password
        self.role = role

users = [
    User('dedede', '123', 'admin'),
    User('supernova', '123', 'selfRegistered')
]

@csrf_protect
def entrance(request):
    form = {'sent': False}
    if(request.method == "POST"):
        form['userlogin'] = request.POST.get('userlogin')
        form['password'] = request.POST.get('password')
        form['role'] = None
        form['sent'] = True

        for user in users:
            if(form['userlogin'] == user.userlogin and form['password'] == user.password):
                form['role'] = user.role
                break

    return render(request, 'entrance.html', context=form)

@csrf_protect
def choice(request):
    form = {'sent': False}
    if(request.method == "POST"):
        form['number1'] = float(request.POST.get('number1'))
        form['number2'] = float(request.POST.get('number2'))
        form['number3'] = float(request.POST.get('number3'))
        form['operation'] = request.POST.get('operation')
        form['sent'] = True

        match form['operation']:
            case 'min':
                form['result'] = min(form['number1'], form['number2'], form['number3'])
            case 'max':
                form['result'] = max(form['number1'], form['number2'], form['number3'])
            case 'avg':
                form['result'] = statistics.mean([form['number1'], form['number2'], form['number3']])

    return render(request, 'choice.html', context=form)

@csrf_protect
def shop(request):
    form = { 'sent': False }
    if(request.method == "POST"):
        form['name'] = request.POST.get('name')
        form['surname'] = request.POST.get('surname')
        form['email'] = request.POST.get('email')
        form['age'] = request.POST.get('age')
        form['address'] = request.POST.get('address')
        form['sex'] = request.POST.get('sex')
        form['agreement'] = True if request.POST.get('agreement') == "agrees" else False
        form['sent'] = True
    return render(request, 'shop.html', context=form)


weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

@csrf_protect
def year(request):
    form = { 'sent': False }
    if(request.method == 'POST'):
        form['year'] = request.POST.get('year')
        isLeap = calendar.isleap(int(form['year']))
        if(isLeap):
            date = datetime.date(int(form['year']), 9, 12)
        else:
            date = datetime.date(int(form['year']), 9, 13)
        form['date'] = f"{date.day} September ({weekdays[date.weekday()]}) {form['year']}"
        form['sent'] = True
    return render(request, 'year.html', context=form)