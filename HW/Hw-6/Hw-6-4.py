# Task - VI
'''
Напишите программу, которая реализует управление данными о студентах университета с помощью текстового файла students.txt. Программа должна предоставлять пользователю меню с возможными действиями:
    Добавить нового студента – пользователь вводит имя, курс и средний балл, программа добавляет их в файл.
    Просмотреть всех студентов – программа загружает и отображает всех студентов, сохранённых в файле.
    Поиск студента по имени – пользователь вводит имя студента, программа выводит информацию о нём.
    Обновить данные студента – пользователь вводит имя студента, программа позволяет обновить его курс и средний балл.
    Удалить студента – пользователь вводит имя студента, и программа удаляет его из файла, если он существует.
    Выход – завершает выполнение программы.
'''

import json
import os

class Student:
    def __init__(self, name: str, year: int, grade: float):
        self.name = name
        self.year = year
        self.grade = grade
    
    def __str__(self) -> str:
        return f"> Name: {self.name}\n> Year: {self.year}\n> Grade: {self.grade}"
    
    def toDictionary(self) -> dict:
        return {
            "name": self.name,
            "year": self.year,
            "grade": self.grade,
        }
    
    @classmethod
    def fromDictionary(cls, data: dict):
        return cls(**data)

class StudentManager:
    students = []

    @staticmethod
    def updateDatabase():
        jsonArray = [student.toDictionary() for student in StudentManager.students]

        with open("students.json", "w", encoding="utf-8") as file:
            json.dump(jsonArray, file, ensure_ascii=False, indent=4)
            file.close()
        return 200

    @staticmethod
    def updateStudentsArray():
        with open("students.json", "r", encoding="utf-8") as file:
            rawJson = json.load(file)
            StudentManager.students = [Student.fromDictionary(student) for student in rawJson]
            file.close()

    @staticmethod
    def getStudents() -> list:
        StudentManager.updateStudentsArray()
        return StudentManager.students
    
    @staticmethod
    def getStudentByName(name: str) -> Student:
        StudentManager.updateStudentsArray()
        for student in StudentManager.students:
            if student.name == name:
                return student
        return None
    
    @staticmethod
    def deleteStudent(name: str) -> int:
        student = StudentManager.getStudentByName(name)
        if student == None:
            return 404
        
        StudentManager.students.remove(student)
        StudentManager.updateDatabase()
        return 200
    
    @staticmethod
    def updateStudent(name: str, year: int, grade: float) -> int:
        student = StudentManager.getStudentByName(name) 
        if student == None:
            return 404
    
        StudentManager.deleteStudent(student.name)
        student.year = year
        student.grade = grade
        StudentManager.students.append(student)

        StudentManager.updateDatabase()
        return 200

    @staticmethod
    def addStudent(newStudent: Student) -> 201:
        try:
            StudentManager.updateStudentsArray()
            StudentManager.students.append(newStudent)
            StudentManager.updateDatabase()
        except Exception as e:
            return f"500: {e}"
        else:
            return 201
    
# Подсмотрел, чтобы чистить консоль
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


while True:
    print("Options:\n> 1 - Add student\n> 2 - View all students\n> 3 - Find by name\n> 4 - Update student\n> 5 - Delete student\n> 0 - Exit")
    choice = int(input("Choice: "))
    match(choice):
        case 1:
            try:
                cls()
                name = input("Enter name: ")
                year = int(input("Enter year: "))
                grade = float(input("Enter grade: "))
                newStudent = Student(name, year, grade)
                statusCode = StudentManager.addStudent(newStudent)
                if(statusCode == 500):
                    raise Exception("Internal error: 500")
            except Exception as e:
                cls()
                print(f"{e}")
            else:
                cls()
                print("201: Created successfully")
            finally:
                input("Press Enter to continue...")
                cls()
        case 2:
            cls()
            print("----- List Of Students -----")
            for student in StudentManager.getStudents():
                print(student, '\n')
            input("\nPress Enter to continue...")
            cls()
        case 3:
            try:
                cls()
                name = input("Enter name: ")
                student = StudentManager.getStudentByName(name)
                if student == None:
                    raise Exception("no such order was found")
            except Exception as e:
                cls()
                print(f"Exception: {e}")
            else:
                cls()
                print(student)
                input("\nPress Enter to continue...")
                cls()
        case 4:
            try:
                cls()
                name = input("Enter name: ")
                year = int(input("Enter year: "))
                grade = float(input("Enter grade: "))
                statusCode = StudentManager.updateStudent(name, year, grade)
                if statusCode == 404:
                    raise Exception("no such student is present in list")
            except Exception as e:
                cls()
                print(f"Exception: {e}")
            else:
                cls()
                print("200: Updated successfully")
                input("\nPress Enter to continue...")
                cls()
        case 5:
            try:
                cls()
                name = input("Enter name: ")
                statusCode = StudentManager.deleteStudent(name)
                if statusCode == 404:
                    raise Exception("no such student is present in list")
            except Exception as e:
                cls()
                print(f"Exception: {e}")
            else:
                cls()
                print("200: Deleted successfully")
                input("\nPress Enter to continue...")
                cls()
        case 0:
            cls()
            print("Exiting...")
            break
        case _:
            print("Invalid input")
            input("Press Enter to continue...")
            cls()