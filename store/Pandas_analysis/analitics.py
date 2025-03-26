import pandas as pd
from s import database
from classes import product

d = ["karl", "mark", 'lora']
s = [2,6,5]

source = pd.Series(d) 


def select_all_products_price(self)-> list[str]:
    query = 'SELECT amount FROM orders'
    self.__cursor = self.__db.cursor()
    self.__cursor.execute(query)
    amount = self.__cursor.fetchall()
    self.__cursor.close()
    return amount

def AllProd(db:database):
    db.open_connections()
    return db.select_all_products()

def convert(products):
    converted_data = []
    for prod in products:
        converted_data.append(product(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5], prod[6]))
    return converted_data

def main():
    db = database() #получить из бд все продукты для посл. конвертации
    all_products = AllProd(db)
    all_products = convert(all_products)
    print(all_products)