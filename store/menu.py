#добавить покупателя (Firstname, Lastname, phone)
#добавить продукт (price, name, isNew, count, idCategory, idCustomer)

from s import database
from classes import product


def secondaryMenuView():
    print('1. вывод всех продуктов')
    print('2. вывод по категории')
    print('3. вывод по цене')
    print('4. вывод по названию')
    print('0. Назад')

def ThirdMenuView():
    print("Выберите продукт") 

def addCustomer(db: database):
    print("Введите данные для регистрации:")
    db.open_connections()
    login = input()
    firstname = input()
    lastname = input()
    phone = int(input())
    db.insert_data_client_by_id([login, firstname, lastname, phone])

def register_customer(db: database):
    db.open_connections()
    print("Введите данные для регистрации:")
    login = input("Логин: ")
    firstname = input("Имя: ")
    lastname = input("Фамилия: ")
    phone = input("Телефон: ")
    customer_id = db.insert_data_client_by_id([login, firstname, lastname, phone])
    return customer_id



def prodAvaible(all_products:list[product], db: database):
    db.open_connections()
    login = input("Логин: ")
    if db.check_if_user_in(login):
        try:
            choice = int(input("Выберите номер продукта для покупки (или 0, чтобы выйти): "))
            if choice == 0:
                print("Выход из выбора продукта.")
                return
            elif 1 <= choice <= len(all_products):
                selected_product = all_products[choice - 1]
                print(f"Вы выбрали продукт: {selected_product}. Он доступен в количестве: {selected_product.count}")

                # Ввод количества для покупки
                quantity = int(input(f"Введите количество {selected_product.name} для покупки: "))
                if quantity > selected_product.count:
                    print(f"Недостаточно {selected_product.name} на складе. Доступное количество: {selected_product.count}.")
                else:
                    print(f"Вы успешно купили {quantity} {selected_product.name}.")
                    # Корректируем оставшийся продукт на складе
                    db.change_data_product_by_id_v2(selected_product.id, selected_product.count - quantity)
                    all_products[selected_product.id].count =  selected_product.count - quantity
                    # Создаем новый заказ
                    db.new_order(selected_product.id, quantity, login)
                    print(f"Количество {selected_product.name} обновлено")
                    print(f"Добавлен новый заказ")
            else:
                print("Неверный номер продукта")
        except ValueError:
            print("введите корректный номер или количество")
    else: print("YOU SHALL NOT PASS")



def ThirdMenu(all_products: list[product], db: database):
        viewAllProducts(all_products)
        prodAvaible(all_products, db)

def viewAllProducts(all_products):
    for product in all_products:
        print(product)

def viewAllProductsByCategory(all_products):
    try:
        category_id = int(input("Введите ID категории для отображения продуктов: "))
        filtered_products = [product for product in all_products if product.idCategory == category_id]

        if filtered_products:
            print(f"Продукты в категории с ID {category_id}:")
            for product in filtered_products:
                print(product)
        else:
            print(f"В категории с ID {category_id} нет продуктов.")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректный ID категории.")



def convert(products):
    converted_data = []
    for prod in products:
        converted_data.append(product(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5], prod[6]))
    return converted_data

def viewAllProducts_price(all_products:list[product]):
    sorted_prod = sorted(all_products, key = lambda x: x.price, reverse = True)
    viewAllProducts(sorted_prod)


def viewAllProducts_name(all_products:list[product]):
    sorted_name = sorted(all_products, key = lambda x: x.name, reverse = False)
    viewAllProducts(sorted_name)


def secondaryMenu(all_products):
    choise = -1
    while choise != 0:
        secondaryMenuView()
        choise = int(input())
        match choise: 
            case 1:
                viewAllProducts(all_products)
            case 2:
                viewAllProductsByCategory(all_products)
            case 3:
                viewAllProducts_price(all_products)
            case 4:
                viewAllProducts_name(all_products)
            case 0:
                main()
secondaryMenu






def addProduct(db: database):
    db.open_connections()
    price = int(input())
    name = input()
    count = int(input())
    db.insert_data_product_by_id([price, name, count])

def menu():
    print('1. добавить покупателя')
    print('2. добавить продукт')
    print('3. далее')
    print('4. купить')
    print('5. регистрация (для покупки необходимо пройти регистрацию)')
    print('0. Закрыть')

def AllProd(db:database):
    db.open_connections()
    return db.select_all_products()
    

def main():
    db = database() #получить из бд все продукты для посл. конвертации
    all_products = AllProd(db)
    all_products = convert(all_products)
    print(all_products)
    choice = -1
    while choice != 0:
        menu()
        choice = int(input())
        match choice: 
            case 1:
                addCustomer(db)
            case 2:
                addProduct()
            case 3:
                print('')
                print('')
                secondaryMenu(all_products)
            case 4:
                print('')
                print('')
                ThirdMenu(all_products, db) 
            case 5:
                register_customer(db)
            case 0:
                print('Закрыть')
main()

