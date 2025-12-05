# Task - V
'''
Напишите программу, которая реализует управление заказами интернет-магазина с помощью текстового файла orders.txt. Программа должна предоставлять пользователю меню с возможными действиями:
    Добавить новый заказ – пользователь вводит номер заказа, название товара, количество и цену, после чего данные добавляются в файл.
    Просмотреть все заказы – программа загружает и отображает все заказы, сохранённые в файле.
    Поиск заказа по номеру – пользователь вводит номер заказа, программа выводит информацию о нём.
    Обновить заказ – пользователь вводит номер заказа, программа позволяет обновить количество и цену товара.
    Удалить заказ – пользователь вводит номер заказа, и программа удаляет его из файла, если он существует.
    Выход – завершает выполнение программы.
'''
import json
import os

class Order:
    def __init__(self, number: int, name: str, price: float, count: int):
        self.number = number
        self.name = name
        self.price = price
        self.count = count
    
    def __str__(self) -> str:
        return f"Order No: {self.number}\n > Name: {self.name}\n > Price: £{self.price}\n > Count: {self.count}"
    
    def toDictionary(self) -> dict:
        return {
            "number": self.number,
            "name": self.name,
            "price": self.price,
            "count": self.count,
        }
    
    @classmethod
    def fromDictionary(cls, data: dict):
        return cls(**data)

class OrderManager:
    orders = []

    @staticmethod
    def updateDatabase():
        jsonArray = [order.toDictionary() for order in OrderManager.orders]

        with open("orders.json", "w", encoding="utf-8") as file:
            json.dump(jsonArray, file, ensure_ascii=False, indent=4)
            file.close()
        return 200

    @staticmethod
    def updateOrdersArray():
        with open("orders.json", "r", encoding="utf-8") as file:
            rawJson = json.load(file)
            OrderManager.orders = [Order.fromDictionary(order) for order in rawJson]
            file.close()

    @staticmethod
    def getOrders() -> list:
        OrderManager.updateOrdersArray()
        return OrderManager.orders
    
    @staticmethod
    def getOrderByNumber(number: int) -> Order:
        OrderManager.updateOrdersArray()
        for order in OrderManager.orders:
            if str(order.number) == str(number):
                return order
        return None
    
    @staticmethod
    def deleteOrder(number: int) -> int:
        order = OrderManager.getOrderByNumber(number)
        if order == None:
            return 404
        
        OrderManager.orders.remove(order)
        OrderManager.updateDatabase()
        return 200
    
    @staticmethod
    def updateOrder(number: int, price: float, count: int) -> int:
        order = OrderManager.getOrderByNumber(number)
        if order == None:
            return 404
    
        OrderManager.deleteOrder(int(order.number))
        order.price = price
        order.count = count
        OrderManager.orders.append(order)

        OrderManager.updateDatabase()
        return 200

    @staticmethod
    def addOrder(newOrder: Order) -> 201:
        try:
            OrderManager.updateOrdersArray()
            OrderManager.orders.append(newOrder)
            OrderManager.updateDatabase()
        except Exception:
            return 500
        else:
            return 201
    
# Подсмотрел, чтобы чистить консоль
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


while True:
    print("Options:\n> 1 - Add order\n> 2 - View all orders\n> 3 - Find by number\n> 4 - Update order\n> 5 - Delete order\n> 0 - Exit")
    choice = int(input("Choice: "))
    match(choice):
        case 1:
            try:
                cls()
                number = int(input("Enter order number: "))
                name = input("Enter name: ")
                price = float(input("Enter price: "))
                count = int(input("Enter count: "))
                newOrder = Order(number, name, price, count)
                statusCode = OrderManager.addOrder(newOrder)
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
            for order in OrderManager.getOrders():
                print("----- List Of Orders -----")
                print(order)
            input("\nPress Enter to continue...")
            cls()
        case 3:
            try:
                cls()
                number = int(input("Enter order number: "))
                order = OrderManager.getOrderByNumber(number)
                if order == None:
                    raise Exception("no such order was found")
            except Exception as e:
                cls()
                print(f"Exception: {e}")
            else:
                cls()
                print(order)
                input("\nPress Enter to continue...")
                cls()
        case 4:
            try:
                cls()
                number = int(input("Enter order number: "))
                price = float(input("Enter price: "))
                count = int(input("Enter count: "))
                statusCode = OrderManager.updateOrder(number, price, count)
                if statusCode == 404:
                    raise Exception("no such order is present in list")
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
                number = int(input("Enter order number: "))
                statusCode = OrderManager.deleteOrder(number)
                if statusCode == 404:
                    raise Exception("no such order is present in list")
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