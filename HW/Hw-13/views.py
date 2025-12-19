from django.shortcuts import render
from django.views import View
from typing import List

class Book:
    def __init__(self, id: int, name: str, author: str, year: int, style: str, publisher: str, isAvailable: bool):
        self.id = id
        self.name = name
        self.author = author
        self.year = year
        self.style = style
        self.publisher = publisher
        self.isAvailable = isAvailable

class Reader:
    def __init__(self, id: int, name: str, surname: str, contacts: str, email: str, registrationDate: str, booksTaken: List[Book], avatar: str):
        self.id = id
        self.name = name
        self.surname = surname
        self.contacts = contacts
        self.email = email
        self.registrationDate = registrationDate
        self.booksTaken = booksTaken
        self.avatar = avatar


books = [
    Book(
        1,
        "Theoretical Physics volume I Mechanics",
        "Evgeny Lifshitz, Lev Landau",
        1935,
        'books/mechanics.png',
        'Physmatlit',
        False
    ),
    Book(
        2,
        "Theoretical Physics volume II Field Theory",
        "Evgeny Lifshitz, Lev Landau",
        1939,
        'books/fieldTheory.png',
        'Physmatlit',
        False
    ),
    Book(
        3,
        "Theoretical Physics volume III Quantum Mechanics",
        "Evgeny Lifshitz, Lev Landau",
        1956,
        'books/quantumMechanics.png',
        'Physmatlit',
        True
    ),
]

readers = [
    Reader(1, "Aqua", "Hoshino", "+000 000 000", "hoshino@gmail.com", "15.01.2025", [], None),
    Reader(2, "Akane", "Kurokawa", "+000 000 000", "akane@gmail.com", "20.11.2025", [books[0], books[1]], 'akane.png'),
    Reader(3, "Ryu", "Lion", "+000 000 000", "lion@gmail.com", "06.04.2025", [], None),
]


def index(request):
    context = {
        "books": books,
        "readers": readers
    }
    return render(request, 'index.html', context=context)

def book(request, id):
    book = next((b for b in books if b.id == id), None)
    context = {"book": book}
    return render(request, 'book.html', context)

def reader(request, id):
    reader = next((r for r in readers if r.id == id), None)
    context = {"reader": reader}
    return render(request, 'reader.html', context)