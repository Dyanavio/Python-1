from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import random
from rest_framework.viewsets import ModelViewSet
from main.models import *
from main.serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework.exceptions import NotFound

cookies = ["Death awaits", "You will feel down for the rest of the week", "You might succeed, or you might not",
           "Be ready for unexpected hardships", "Luck is clearly not on your side"]

@api_view()
def cookieView(request: Request) -> Response:
    return Response({"cookie": f"{cookies[random.randrange(0, len(cookies))]}"})

@api_view()
def randomNumber(request: Request) -> Response:
    return Response({"result": int(random.random() * 100)})

@api_view()
def randomNumberInRange(request: Request, begin: int, end: int) -> Response:
    return Response({ "result":  random.randint(begin, end) })

@api_view()
def randomRange(request: Request, size: int) -> Response:
    if size <= 0:
        return Response({"status": "406 Not Acceptable", "message": "Input natural number only"})
    return Response({ "result": list(int(random.random() * 100) for i in range(0, size)) })

@api_view()
def randomPoem(request: Request) -> Response:
    initialize()
    poems = Poem.objects.all()
    poem = poems[random.randrange(0, len(poems))]
    serialized = PoemSerializer(poem)
    return Response({"poem" : serialized.data })

@api_view()
def randomPoemAuthor(request: Request, author: str) -> Response:
    initialize()
    poems = Poem.objects.filter(author__name=author)
    if poems.count() == 0:
        raise NotFound(detail="No such author exists", code=404)
    poem = poems[random.randrange(0, len(poems))]
    serialized = PoemSerializer(poem)
    return Response({"poem" : serialized.data })

@api_view()
def randomPoemTheme(request: Request, theme: str) -> Response:
    poems = Poem.objects.filter(theme__name=theme)
    if poems.count() == 0:
        raise NotFound(detail="No such theme found", code=404)
    poem = poems[random.randrange(0, len(poems))]
    serialized = PoemSerializer(poem)
    return Response({ "poem": serialized.data })

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ThemeViewSet(ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer

class PoemFilter(django_filters.FilterSet):
    class Meta:
        model = Poem
        fields = [
            "name",
            "author__name",
            "theme__name",
        ] 

class PoemViewSet(ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    filter_backends = [ SearchFilter, DjangoFilterBackend, OrderingFilter ]
    filterset_class = PoemFilter
    serach_fields = ["name", "author__name", "theme__name"]














def initialize():
    authors = [
        Author(name="Romino"),
        Author(name="Pushkin"),
        Author(name="Shakespeare"),
        Author(name="Toth")
    ]
    themes = [
        Theme(name="Love"),
        Theme(name="Despair")
    ]
    poems = [
        Poem(name="Her", author=authors[1], theme=themes[0]),
        Poem(name="The Tenth Commandment", author=authors[1], theme=themes[0]),
        Poem(name="Pharloom's Folly", author=authors[0], theme=themes[1]),
        Poem(name="The Earth", author=authors[3], theme=themes[1]),
        Poem(name="No longer mourn for me when I am dead", author=authors[2], theme=themes[1])
    ]
    if Author.objects.all().count() == 0:
        for author in authors: 
            author.save()
    if Theme.objects.all().count() == 0:
        for theme in themes: 
            theme.save()
    if Poem.objects.all().all().count() == 0:
        for poem in poems: 
            poem.save()