from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse


def nav():
    links = [
        ("Main Page", "main"),
        ("News", "news"),
        ("Government", "government"),
        ("Facts", "facts"),
        ("Contacts", "contacts"),
        ("History", "history")
    ]
    items = "  |  ".join([f'<a href="{reverse(name)}">{title}</a>' for title, name in links])
    return f'<nav style="margin-bottom:12px;">{items}</nav>'

def index(request):
     return HttpResponse(f'{nav()}<h1>Main page</h1>{""}<i>Town\'s main page</i>')

def news(request):
    return HttpResponse(f'{nav()}<h1>News</h1>{""}<i>There has been no news to report for today</i>')

def government(request):
    return HttpResponse(f'{nav()}<h1>Local Government</h1>{""}<i>is dull</i>')

def facts(request):
    return HttpResponse(f'{nav()}<h1>Facts</h1>{""}<i>Historical facts of this town were erased from history</i>')

def contacts(request):
    return HttpResponse(
        f"""{nav()}
        <h1>Contacts</h1>
        <ul>
            <li>Mayor's office - 048 722 7501</li>
            <li>Translation Agency - 067 192 6481</li>
            <li>Court - 048 753 1828</li>
        </ul>
        """
    )

def history(request):
    return HttpResponse(
       f""" 
            {nav()}
            <h1>History</h1>
            <ul>
                <a href={reverse('historyTopic', args=['people'])}><li>People</li></a>
                <a href={reverse('historyTopic', args=['photoes'])}><li>Photoes</li></a>
            </ul>
        """
    )

def historyTopic(request, topic: str):
    topic = topic.strip().lower()
    if(topic == 'people'):
        info = """
                <h1>Famous people</h1>
                <ul>
                    <li>Grigorii Mikhailovich Fikhtengol'ts</li>
                    <li>Emil Gilels</li>
                </ul>
            """
    elif(topic == 'photoes'):
        info = """
                <h1>Photoes</h1>
                <img src="https://placehold.co/600x400/orange/white/?text=Pushkin"/>
            """
    return HttpResponse(f"{nav()}{info}")