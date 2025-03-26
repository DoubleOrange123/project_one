import pandas as pd
from s import database
from classes import order



def select_all_orders(self)-> list[str]:
    query = 'SELECT order_date, amount FROM orders'
    self.__cursor = self.__db.cursor()
    self.__cursor.execute(query)
    data = self.__cursor.fetchall()
    self.__cursor.close()
    return data

def All_Orders(db:database):
    db.open_connections()
    return db.select_all_orders()

def convert(orders):
    converted_data = []
    for ord in orders:
        converted_data.append(order(order_date = ord[0], amount = ord[1]))
    for obj in converted_data:
        print(f"Order Date: {obj.order_date}, Amount: {obj.amount}")
    return converted_data


def pandas_order(obj_list: list[order]):
    total_amount_per_date = {}  # Словарь для подсчета общего количества товаров по дате
    for obj in obj_list:
        order_date = obj.order_date
        amount = obj.amount
        if order_date in total_amount_per_date:
            total_amount_per_date[order_date] += amount  # Увеличиваем общее количество для этой даты
        else:
            total_amount_per_date[order_date] = amount  # Инициализируем общее количество для новой даты

    # Находим максимальное количество купленных товаров
    max_amount = max(total_amount_per_date.values())
    
    # Находим все даты, у которых количество купленных товаров соответствует максимальному
    busiest_dates = [date for date, total in total_amount_per_date.items() if total == max_amount]

    print(f"{busiest_dates}, {max_amount}")  # Печатаем результат
    
def main():
    db = database()
    db.open_connections()
    data = db.select_all_orders()
    objects = convert(data)
    pandas_order(objects)
main()
