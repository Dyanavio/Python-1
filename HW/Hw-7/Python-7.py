from dataclasses import dataclass
from typing import List, Dict, Any
import sqlite3
import os
from abc import ABC, abstractmethod


@dataclass
class Actor:
    name: str
    role: str

@dataclass
class Film:
    name: str
    genre: str
    director: str
    year: int
    duration: str
    studio: str
    actors: Dict[str, str]

class FilmAccessor:
    def __init__(self, dbPath: str = "film.db"):
        self.dbPath = dbPath
        self.__createTable()

    def __connect(self):
        return sqlite3.connect(self.dbPath)

    def __createTable(self):
        connection = self.__connect()
        cursor = connection.cursor()
        cursor.execute("""
                    Create table if not exists films (
                            id integer primary key autoincrement,
                            name text not null,
                            genre text not null,
                            director text not null,
                            year integer not null,
                            duration text not null,
                            studio text not null,
                            actors text not null
                        );
                    """)
        connection.commit()
        connection.close()

    
    def addFilm(self, film: Film) -> None:
        connection = self.__connect()
        cursor = connection.cursor()
        cursor.execute("""
                        Insert into films (name, genre, director, year, duration, studio, actors)
                        Values(?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        film.name,
                        film.genre,
                        film.director,
                        film.year,
                        film.duration,
                        film.studio,
                        str(film.actors)
                    )
                )
        connection.commit()
        connection.close()

    def getFilms(self) -> List[Film]:
        connection = self.__connect()
        cursor = connection.cursor()
        cursor.execute("SELECT name, genre, director, year, duration, studio, actors FROM films")
        rows = cursor.fetchall()
        connection.close()
        return [
            Film(
                name=row[0],
                genre=row[1],
                director=row[2],
                year=row[3],
                duration=row[4],
                studio=row[5],
                actors=eval(row[6]),
            ) for row in rows
        ]
    
class FilmTemplate(ABC):
    @abstractmethod
    def render(self, films: List[Film]) -> str:
        pass

class FilmTableTemplate(FilmTemplate):
    def render(self, films: List[Film]) -> str:
        result = "\n" + 210*"-" + "\n"
        for film in films:
            result += f"{film.name:20}|{film.genre:15}|{film.director:15}|{film.year:8}|{film.duration:8}|{film.studio:15}|{film.actors}\n"
        result += 210*"-" + "\n"
        return result

class FilmSimpleTemplate(FilmTemplate):
    def render(self, films: List[Film]) -> str:
        result = ""
        for film in films:
            result += f"{film.name} in {film.year} by {film.studio}\n"
        return result
    
class FilmView:
    def __init__(self, model: FilmAccessor) -> None:
        self.model = model
    
    def render(self, template: FilmTemplate) -> str:
        films = self.model.getFilms()
        return template.render(films)
    
def inputFilm() -> Film:
    name = input("Input the name of the film: ")
    genre = input("Input genre: ")
    director = input("Input director: ")
    year = int(input("Input year: "))
    duration = input("Input duration: ")
    studio = input("Input studio: ")
    castCount = int(input("Input the number of actors: "))

    actors = dict()
    for i in range(0, castCount):
        actorName = input(f"{i}) Input actor's name: ")
        actorRole = input(f"{i}) Input actor's role: ")
        actors[actorName] = actorRole
        print()

    return Film(name, genre, director, year, duration, studio, actors)

def showMenu() -> int:
    print("*" * 80)
    print("1 - Add a film\n2 - Show films (table style)\n3 - Show films (list style)\n0 - Exit")
    choice = int(input("Choice: "))
    print("*" * 80)
    return choice

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

modelObject = FilmAccessor()
viewObject = FilmView(modelObject)
tableTemplate = FilmTableTemplate()
simpleTemplate = FilmSimpleTemplate()

while True:
    choice = showMenu()
    match choice:
        case 1:
            cls()
            modelObject.addFilm(inputFilm())
            cls()
        case 2:
            cls()
            print(viewObject.render(tableTemplate))
            input("Press Enter to continue...")
            cls()
        case 3:
            cls()
            print(viewObject.render(simpleTemplate))
            input("Press Enter to continue...")
            cls()
        case 0:
            cls()
            print("Exiting...")
            break
        case _:
            cls()
            print("Invalid input")
            input("Press Enter to continue...")
            cls()