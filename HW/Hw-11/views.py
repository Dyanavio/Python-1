from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.core.serializers.json import DjangoJSONEncoder
from django.views import View

def nav():
    links = [
        ("Main Page", "main"),
        ("History", "history"),
        ("Cities", "citiesAll"),
        ("Facts", "facts")
    ]
    items = "  |  ".join([f"<a href='{reverse(name)}'>{title}</a>" for title, name in links])
    return f'<nav style="margin-bottom:12px;">{items}</nav>'

def index(request):
    return HttpResponse(f"{nav()}<h1>France</h1>")

def history(request):
    return HttpResponse(f"""
                        {nav()}
                        <h1>History</h1>
                        <ul>
                            <a href="{reverse("historyYear", args=[1895])}"><li>1895</li></a>
                            <a href="{reverse("historyYear", args=[1914])}"><li>1914</li></a>
                        </ul>
                        """)

def historyYear(request, year: int):
    info = f"{nav()}"
    if(str(year) == "1914"):
        info += f"""
                            <h1>France in 1914</h1>
                            <ul>
                                <li>6–8 September – French Army troops are rushed from Paris to join the First Battle of the Marne using Renault Type AG taxicabs.</li>
                                <li>13 September – The conclusion of the Battle of Grand Couronné ends the Battle of the Frontiers, with the north-east segment of the Western Front stabilising.</li>
                                <li>25 September – Battle of Albert begins as part of the Race to the Sea.</li>
                                <li>27 September – First Battle of Artois begins.</li>
                                <li>28 September – The First Battle of the Aisne ends indecisively.</li>
                                <li>30 September – British Indian Army Expeditionary Force A arrives at Marseille for service on the Western Front.</li>
                                <li>1 October – Battle of Arras begins.</li>
                                <li>4 October – Lens is lost, as French Tenth Army fails to hold back the Germans.</li>
                                <li>5 October – Aerial combat of 5 October 1914</li>
                                <li>4 November – Britain and France declare war on the Ottoman Empire.</li>
                                <li>20 December – First Battle of Champagne begins.</li>
                            </ul>
                        """
    elif(str(year) == "1895"):
        info += f"""
                <h1>France in 1895</h1>
                <ul>
                    <li>1 January – Alphonse Mucha's lithographed poster for the play Gismonda starring Sarah Bernhardt is posted in Paris. Bernhardt is so satisfied with its success that she gives Mucha a six-year contract.</li>
                    <li>5 January – The military degradation of Alfred Dreyfus takes place on the Champ de Mars, Paris.</li>
                    <li>17 January – Félix Faure is elected President of French Republic after the resignation of Jean Casimir-Perier.</li>
                    <li>17 January – Dreyfus is moved into a military reformatory on the island of Ré.</li>
                    <li>21 February – Dreyfus is put on board ship to be exiled.</li>
                    <li>15 March – Dreyfus is landed on Devil's Island off French Guiana.</li>
                    <li>22 March – Brothers Auguste and Louis Lumière make what is probably the first presentation of a projected celluloid film moving picture, the 46-second Workers Leaving the Lumière Factory, to members of the Société d'encouragement pour l'industrie nationale in Paris.</li>
                </ul>
                """
    else:
        return HttpResponseRedirect('/history/')
    return HttpResponse(info)

def citiesAll(request):
    return HttpResponse(f"""
                            {nav()}
                            <h1>French Cities</h1>
                            <ul>
                                <li>Paris</li>
                                <li>Bordeaux</li>
                                <li>Toulouse</li>
                                <li>Marseille</li>
                                <li>Lyon</li>
                                <li>Strasbourg</li>
                                <li>Lille</li>
                            </ul>
                        """)

def citites(request, city):
    info = ""
    if(city == "Paris"):
        info = """
                <h1>Paris</h1>
                <i>Something about Paris</i>    
            """
    elif(city == "Bordeaux"):
        info = """
                <h1>Bordeaux</h1>
                <i>Something about Bordeaux</i>    
            """
    elif(city == "Toulouse"):
        info = """
                <h1>Toulouse</h1>
                <i>Something about Toulouse</i>    
            """
    elif(city == "Marseille"):
        info = """
                <h1>Marseille</h1>
                <i>Something about Marseille</i>    
            """
    elif(city == "Lyon"):
        info = """
                <h1>Lyon</h1>
                <i>Something about Lyon</i>    
            """
    elif(city == "Strasbourg"):
        info = """
                <h1>Strasbourg</h1>
                <i>Something about Strasbourg</i>    
            """
    elif(city == "Lille"):
        info = """
                <h1>Lille</h1>
                <i>Something about Lille</i>    
            """
    else:
        return HttpResponseRedirect("/cities/")

    return HttpResponse(info)

def cityYear(request, city, year):
    info = f"{nav()}"
    if(city == "Paris" and year == 1940):
        info += f"""
                <h1>1940 in Paris</h1>
                <p>The Battle of France (French: bataille de France; 10 May – 25 June 1940), also known as the Western Campaign (German: Westfeldzug), the French Campaign (Frankreichfeldzug, campagne de France) and the Fall of France, during the Second World War was the German invasion of the Low Countries (Belgium, Luxembourg and the Netherlands) and France. The plan for the invasion of the Low Countries and France was called Fall Gelb (Case Yellow or the Manstein plan). Fall Rot (Case Red) was planned to finish off the French and British after the evacuation at Dunkirk. The Low Countries and France were defeated and occupied by Axis troops down to the Demarcation line.</p>
                """
    elif(city == "Marseille" and year == 1940):
        info += f"""
                <h1>1940 in Marseille</h1>
                <p>Bombing of Marseille</p>
                """
    else:
        return HttpResponseRedirect('/history/')
    return HttpResponse(info)
    
def city(request):
    name = request.GET.get('city')
    year = request.GET.get('year')
    return HttpResponseRedirect(f"/cities/{name}/{year}")

def facts(request):
    return HttpResponse(f"{nav()}<h1>Facts</h1>")
