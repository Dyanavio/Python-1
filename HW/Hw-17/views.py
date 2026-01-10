from main.models import *
from main.forms import *
from django.views.decorators.csrf import csrf_protect
from django.core.files.storage import FileSystemStorage
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404

@login_required
@permission_required("main.view_book", raise_exception=True)
def index(request):
    initialize()
    currentDisplay = 'all'
    if request.method == "POST":
        if request.POST.get("currentDisplay") == "all":
            currentDisplay = "availableOnly"
    books = Book.objects.all()
    readers = Reader.objects.all()
    return render(request, "index.html", context={"readers": readers, "books": books, "currentDisplay": currentDisplay})


@permission_required("main.view_book", raise_exception=True)
def book(request, id):
    book = Book.objects.get(pk = id)
    return render(request, "book.html", context={"book": book})


@permission_required("main.view_reader", raise_exception=True)
def reader(request, id):
    reader = Reader.objects.get(pk = id)
    return render(request, "reader.html", context={"reader": reader})


@csrf_protect
@permission_required("main.add_book", raise_exception=True)
def createBook(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if(form.is_valid()):
            style = None
            if "style" in request.FILES:
                styleFile = request.FILES["style"]
                fileSystemStorage = FileSystemStorage(location='media/pictures/books')
                filename = fileSystemStorage.save(styleFile.name, styleFile)
                style = filename

            book = Book()
            book.name = form.cleaned_data["name"]
            book.author = form.cleaned_data["author"]
            book.year = int(form.cleaned_data["year"])
            book.style = style
            book.publisher = form.cleaned_data["publisher"]
            book.isAvailable = bool(form.cleaned_data["isAvailable"])
        
            book.save()

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
@permission_required("main.add_reader", raise_exception=True)
def createReader(request):
    if request.method == "POST":
        form = ReaderForm(request.POST, request.FILES)
        if(form.is_valid()):
            avatar = None
            if "avatar" in request.FILES:
                avatarFile = request.FILES["avatar"]
                fileSystemStorage = FileSystemStorage(location='media/pictures/readers')
                filename = fileSystemStorage.save(avatarFile.name, avatarFile)
                avatar = filename
            
            reader = Reader()
            reader.name = form.cleaned_data["name"]
            reader.surname = form.cleaned_data["surname"]
            reader.contacts = str(form.cleaned_data["contacts"])
            reader.email = form.cleaned_data["email"]
            reader.registrationDate = form.cleaned_data["registrationDate"]
            reader.booksTaken = None
            reader.avatar = avatar

            reader.save()
            
            return render(request, "createReader.html", context={
                "form": ReaderForm(), 
                "success": True,
                "message": f"Reader '{reader.name}' added successfully!"
            })
    else:
        form = ReaderForm()

    context = {"form": form, "success": False}
    return render(request, "createReader.html", context)


@csrf_protect
@permission_required("main.change_book", raise_exception=True)
def updateBook(request, bookId):
    book = Book.objects.get(pk = bookId)

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

            book.save()
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
                    "bookId": book.pk,
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
@permission_required("main.change_reader", raise_exception=True)
def updateReader(request, readerId):
    reader = Reader.objects.get(pk = readerId)

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

            booksIds = request.POST.getlist("booksTaken")
            booksTaken = Book.objects.filter(id__in=booksIds)
            for book in reader.booksTaken.all():
                book.isAvailable = True
                book.save()

            reader.booksTaken.set(booksTaken)
            for book in booksTaken:
                book.isAvailable = False
                book.save()
            
            if "avatar" in request.FILES:
                avatarFile = request.FILES["avatar"]
                fileSystemStorage = FileSystemStorage(location='media/pictures/readers')
                filename = fileSystemStorage.save(avatarFile.name, avatarFile)
                reader.avatar = filename
            
            reader.save()
            return render(
                request,
                "updateReader.html",
                {
                    "form": ReaderForm(
                        initial={
                            "name": reader.name,
                            "surname": reader.surname,
                            "contacts": reader.contacts,
                            "registrationDate": reader.registrationDate,
                            "email": reader.email,
                            "booksTaken": reader.booksTaken,
                        }
                    ),
                    "books": Book.objects.all(),
                    "bookIds": reader.booksTaken.values_list("id", flat=True),
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
                "registrationDate": reader.registrationDate,
                "email": reader.email,
                "booksTaken": reader.booksTaken,
            }
        )
    context = {"form": form, "reader": reader, "readerId": reader.id, "success": False, "books": Book.objects.all(), "bookIds": reader.booksTaken.values_list("id", flat=True),}
    return render(request, "updateReader.html", context)


@csrf_protect
@permission_required("main.delete_book", raise_exception=True)
def deleteBook(request, bookId):
    book = Book.objects.get(pk = bookId)

    if book is None:
        context = {"error": "Book was not found"}
        return render(request, "deleteBook.html", context)

    if request.method == "POST":
        if "confirm" in request.POST:
            fileSystemStorage = FileSystemStorage(location="media/pictures/books")
            if fileSystemStorage.exists(str(book.style)):  
                fileSystemStorage.delete(str(book.style))

            bookName = book.name
            book.delete()
            return render(
                request,
                "deleteBook.html",
                {
                    "success": True,
                    "message": f"Book '{bookName}' was deleted successfully!",
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
@permission_required("main.delete_reader", raise_exception=True)
def deleteReader(request, readerId):
    reader = Reader.objects.get(pk = readerId)

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

            readerName = f"{reader.name} {reader.surname}"
            reader.delete()
            return render(
                request,
                "deleteReader.html",
                {
                    "success": True,
                    "message": f"Reader '{readerName}' was deleted successfully!",
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



def initialize():
    books = [
        Book(
            name        = "Theoretical Physics volume I Mechanics",
            author      = "Evgeny Lifshitz, Lev Landau",
            year        = 1935,
            style       = 'mechanics.png',
            publisher   = 'Physmatlit',
            isAvailable = True
        ),
        Book(
            name        = "Theoretical Physics volume II Field Theory",
            author      = "Evgeny Lifshitz, Lev Landau",
            year        = 1939,
            style       = 'fieldTheory.png',
            publisher   = 'Physmatlit',
            isAvailable = True
        ),
        Book(
            name        = "Theoretical Physics volume IV Quantum Electordynamics",
            author      = "Evgeny Lifshitz, Lev Landau",
            year        = 1956,
            style       = 'quantumElectrodynamics.png',
            publisher   = 'Physmatlit',
            isAvailable = True
        ),
    ]

    readers = [
        Reader(name="Aqua", surname="Hoshino", contacts="+000 000 000", email="hoshino@gmail.com", registrationDate=datetime.date(2025, 1, 15), avatar="nouser.png"),
        Reader(name="Akane", surname="Kurokawa", contacts="+000 000 000", email="akane@gmail.com", registrationDate=datetime.date(2025, 11, 20), avatar='akane.png'),
        Reader(name="Ryu", surname="Lion", contacts="+000 000 000", email="lion@gmail.com", registrationDate=datetime.date(2025, 4, 6), avatar="nouser.png"),
    ]

    if Book.objects.all().count() == 0:
        for book in books:
            book.save()
    if Reader.objects.all().count() == 0:
        for reader in readers:
            reader.save()