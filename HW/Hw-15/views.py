from django.shortcuts import render
from django.views import View
from typing import List
from main.forms import *
from django.views.decorators.csrf import csrf_protect
from django.core.files.storage import FileSystemStorage
import datetime

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
        'mechanics.png',
        'Physmatlit',
        False
    ),
    Book(
        2,
        "Theoretical Physics volume II Field Theory",
        "Evgeny Lifshitz, Lev Landau",
        1939,
        'fieldTheory.png',
        'Physmatlit',
        False
    ),
    Book(
        3,
        "Theoretical Physics volume III Quantum Mechanics",
        "Evgeny Lifshitz, Lev Landau",
        1956,
        'quantumMechanics.png',
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

# CREATE
@csrf_protect
def createBook(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if(form.is_valid()):
            id = max([book.id for book in books]) + 1 if books else 1
            
            style = None
            if "style" in request.FILES:
                styleFile = request.FILES["style"]
                fileSystemStorage = FileSystemStorage(location='media/pictures/books')
                filename = fileSystemStorage.save(styleFile.name, styleFile)
                style = filename
            
            book = Book(
                id,
                form.cleaned_data["name"],
                form.cleaned_data["author"],
                int(form.cleaned_data["year"]),
                style,
                form.cleaned_data["publisher"],
                bool(form.cleaned_data["isAvailable"])
            )

            books.append(book)
            return render(request, "createBook.html", context={
                "form": BookForm(), 
                "success": True,
                "message": f"Book '{book.name}' added successfully!"
            })
    else:
        form = BookForm()

    context = {"form": form, "success": False}
    return render(request, "createBook.html", context)


@csrf_protect
def createReader(request):
    if request.method == "POST":
        form = ReaderForm(request.POST, request.FILES)
        if(form.is_valid()):
            id = max([reader.id for reader in readers]) + 1 if readers else 1
            
            avatar = None
            if "avatar" in request.FILES:
                avatarFile = request.FILES["avatar"]
                fileSystemStorage = FileSystemStorage(location='media/pictures/readers')
                filename = fileSystemStorage.save(avatarFile.name, avatarFile)
                avatar = filename
            
            reader = Reader(
                id,
                form.cleaned_data["name"],
                form.cleaned_data["surname"],
                str(form.cleaned_data["contacts"]),
                form.cleaned_data["email"],
                form.cleaned_data["registrationDate"],
                [],
                avatar
            )

            readers.append(reader)
            return render(request, "createReader.html", context={
                "form": ReaderForm(), 
                "success": True,
                "message": f"Reader '{reader.name}' added successfully!"
            })
    else:
        form = ReaderForm()

    context = {"form": form, "success": False}
    return render(request, "createReader.html", context)


# Update
@csrf_protect
def updateBook(request, bookId):
    book = next((b for b in books if b.id == bookId), None)

    if book is None:
        context = {"error": "Book was not found"}
        return render(request, "updateBook.html", context)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book.name = form.cleaned_data["name"]
            book.author = form.cleaned_data["author"]
            book.year = form.cleaned_data["year"]
            book.publisher = form.cleaned_data["publisher"]
            book.isAvailable = form.cleaned_data["isAvailable"]

            if "style" in request.FILES:
                styleFile = request.FILES["style"]
                fileSystemStorage = FileSystemStorage(location='media/pictures/books')
                filename = fileSystemStorage.save(styleFile.name, styleFile)
                book.style = filename

            return render(
                request,
                "updateBook.html",
                {
                    "form": BookForm(
                        initial={
                            "name": book.name,
                            "author": book.author,
                            "year": book.year,
                            "publisher": book.publisher,
                            "isAvailable": book.isAvailable,
                        }
                    ),
                    "bookId": book.id,
                    "success": True,
                    "message": f"Book '{book.name}' was updated successfully!",
                },
            )
    else:
        form = BookForm(
            initial={
                "name": book.name,
                "author": book.author,
                "year": book.year,
                "publisher": book.publisher,
                "isAvailable": book.isAvailable,
            }
        )

    context = {"form": form, "book": book, "film_id": book.id, "success": False}
    return render(request, "updateBook.html", context)


@csrf_protect
def updateReader(request, readerId):
    reader = next((r for r in readers if r.id == readerId), None)

    if reader is None:
        context = {"error": "Reader was not found"}
        return render(request, "updateReader.html", context)

    if request.method == "POST":
        form = ReaderForm(request.POST, request.FILES)
        if form.is_valid():
            reader.name = form.cleaned_data["name"]
            reader.surname = form.cleaned_data["surname"]
            reader.contacts = form.cleaned_data["contacts"]
            reader.email = form.cleaned_data["email"]
            #reader.booksTaken = form.cleaned_data["booksTaken"]
            booksList = eval(form.cleaned_data["booksTaken"])
            for book in booksList:
                id = book[0]
                if any(b.id == id and not reader.booksTaken.__contains__(b) for b in books):
                    reader.booksTaken.append(books[id - 1])


            if "avatar" in request.FILES:
                avatarFile = request.FILES["avatar"]
                fileSystemStorage = FileSystemStorage(location='media/pictures/readers')
                filename = fileSystemStorage.save(avatarFile.name, avatarFile)
                reader.avatar = filename

            return render(
                request,
                "updateReader.html",
                {
                    "form": ReaderForm(
                        initial={
                            "name": reader.name,
                            "surname": reader.surname,
                            "contacts": reader.contacts,
                            "registrationDate": datetime.date.strptime(reader.registrationDate, "%d.%m.%Y"),
                            "email": reader.email,
                            "booksTaken": reader.booksTaken,
                        }
                    ),
                    "readerId": reader.id,
                    "success": True,
                    "message": f"Reader '{reader.name} {reader.surname}' was updated successfully!",
                },
            )
    else:
        form = ReaderForm(
            initial={
                "name": reader.name,
                "surname": reader.surname,
                "contacts": reader.contacts,
                "registrationDate": datetime.date.strptime(reader.registrationDate, "%d.%m.%Y"),
                "email": reader.email,
                "booksTaken": [(book.id, book.name) for book in reader.booksTaken],
            }
        )

    context = {"form": form, "reader": reader, "readerId": reader.id, "success": False}
    return render(request, "updateReader.html", context)


# Delete
@csrf_protect
def deleteBook(request, bookId):
    book = next((b for b in books if b.id == bookId), None)

    if book is None:
        context = {"error": "Book was not found"}
        return render(request, "deleteBook.html", context)

    if request.method == "POST":
        if "confirm" in request.POST:
            fileSystemStorage = FileSystemStorage(location="media/pictures/books")
            if fileSystemStorage.exists(str(book.style)):  
                fileSystemStorage.delete(str(book.style))

            books.remove(book)
            return render(
                request,
                "deleteBook.html",
                {
                    "success": True,
                    "message": f"Book '{book.name}' was deleted successfully!",
                },
            )
        else:
            context = {"book": book, "bookId": book.id, "success": False}
            return render(request, "deleteBook.html", context)

    context = {
        "book": book,
        "bookId": book.id,
        "confirm_required": True,
        "success": False,
    }
    return render(request, "deleteBook.html", context)


@csrf_protect
def deleteReader(request, readerId):
    reader = next((r for r in readers if r.id == readerId), None)

    if reader is None:
        context = {"error": "Reader was not found"}
        return render(request, "deleteReader.html", context)

    if request.method == "POST":
        if "confirm" in request.POST:
            fileSystemStorage = FileSystemStorage(location="media/pictures/readers")
            if fileSystemStorage.exists(str(reader.avatar)):  
                fileSystemStorage.delete(str(reader.avatar))

            for book in reader.booksTaken:
                book.isAvailable = True

            readers.remove(reader)
            return render(
                request,
                "deleteReader.html",
                {
                    "success": True,
                    "message": f"Reader '{reader.name} {reader.surname}' was deleted successfully!",
                },
            )
        else:
            context = {"reader": reader, "readerId": reader.id, "success": False}
            return render(request, "deleteReader.html", context)

    context = {
        "reader": reader,
        "readerId": reader.id,
        "confirm_required": True,
        "success": False,
    }
    return render(request, "deleteReader.html", context)

