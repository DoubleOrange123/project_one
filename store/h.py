class Product:
    def __init__(self, id: int, price: int, name: str, isNew: bool, count: int, idCategory: int, idCustomer: int):
        self.id = id
        self.price = price
        self.name = name
        self.isNew = isNew
        self.count = count
        self.idCategory = idCategory
        self.idCustomer = idCustomer

    def __str__(self):
        return f'{self.id} {self.price} {self.name} {self.isNew} {self.count} {self.idCategory} {self.idCustomer}'

class Database:
    def open_connections(self):
        # Код для открытия соединения с базой данных
        pass

    def close_connections(self):
        # Код для закрытия соединений с базой данных
        pass

    def select_all_products(self):
        # Логика получения всех продуктов
        pass
    
    def insert_data_client_by_id(self, data):
        # Код для добавления клиента в базу
        pass

    def insert_data_product_by_id(self, data):
        # Код для добавления продукта в базу
        pass

    # Другие методы для выборки по категориям, цене и названию


def secondaryMenuView():
    print('1. вывод всех продуктов')
    print('2. вывод по категории')
    print('3. вывод по цене')
    print('4. вывод по названию')
    print('0. Назад')

def viewAllProducts(db: Database):
    db.open_connections()
    products = db.select_all_products()
    for product in products:
        print(product)
    db.close_connections()

def viewAllProducts_category(db: Database):
    category_id = int(input("Введите ID категории: "))
    db.open_connections()
    products = db.select_products_by_category(category_id)
    for product in products:
        print(product)
    db.close_connections()

def viewAllProducts_price(db: Database):
    min_price = int(input("Введите минимальную цену: "))
    max_price = int(input("Введите максимальную цену: "))
    db.open_connections()
    products = db.select_products_by_price(min_price, max_price)
    for product in products:
        print(product)
    db.close_connections()

def viewAllProducts_name(db: Database):
    name_query = input("Введите название продукта для поиска: ")
    db.open_connections()
    products = db.select_products_by_name(name_query)
    for product in products:
        print(product)
    db.close_connections()

def secondaryMenu(db: Database):
    choice = -1
    while choice != 0:
        secondaryMenuView()
        choice = int(input("Выберите вариант: "))
        match choice: 
            case 1:
                viewAllProducts(db)
            case 2:
                viewAllProducts_category(db)
            case 3:
                viewAllProducts_price(db)
            case 4:
                viewAllProducts_name(db)
            case 0:
                print("Возврат в главное меню")

def addCustomer(db: Database):
    db.open_connections()
    firstname = input("Введите имя: ")
    lastname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    db.insert_data_client_by_id([firstname, lastname, phone])
    db.close_connections()

def addProduct(db: Database):
    db.open_connections()
    price = int(input("Введите цену: "))
    name = input("Введите название: ")
    count = int(input("Введите количество: "))
    db.insert_data_product_by_id([price, name, count])
    db.close_connections()

def menu():
    print('1. добавить покупателя')
    print('2. добавить продукт')
    print('3. далее')
    print('0. Закрыть')

def main():
    db = Database()
    choice = -1
    while choice != 0:
        menu()
        choice = int(input("Выберите вариант: "))
        match choice: 
            case 1:
                addCustomer(db)
            case 2:
                addProduct(db)
            case 3:
                secondaryMenu(db)
            case 0:
                print('Закрытие программы')
                break

if __name__ == "__main__":
    main()