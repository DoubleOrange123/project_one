# Меню
def menu():
    print("1. Добавить покупателя")
    print("2. Добавить продукт")
    print("3. Просмотреть продукты")
    print("4. Покупить продукт")
    print("0. Выход")


def secondaryMenuView():
    print("1. Показать все продукты")
    print("2. Поиск по категории")
    print("3. Сортировать по цене")
    print("4. Сортировать по названию")
    print("0. Назад")


def ThirdMenuView():
    print("Выберите продукт")


def viewAllProducts(all_products):
    for product in all_products:
        print(product)


def viewAllProductsByCategory(all_products):
    category_id = int(input("Введите ID категории: "))
    products = [p for p in all_products if p.idCategory == category_id]
    if products:
        for product in products:
            print(product)
    else:
        print("Продуктов в этой категории нет.")


def viewAllProducts_price(all_products):
    sorted_products = sorted(all_products, key=lambda p: p.price)
    for product in sorted_products:
        print(product)


def viewAllProducts_name(all_products):
    sorted_products = sorted(all_products, key=lambda p: p.name)
    for product in sorted_products:
        print(product)


def prodAvaible(all_products, db):
    choice = int(input("Выберите номер продукта для покупки (или 0, чтобы выйти): "))
    if choice == 0:
        print("Выход из выбора продукта.")
        return
    elif choice >= 1 and choice <= len(all_products):
        selected_product = all_products[choice - 1]
        print(f"Вы выбрали {selected_product.name}, его количество: {selected_product.count}.")
        quantity = int(input(f"Сколько {selected_product.name} вы хотите купить? "))
        if quantity > selected_product.count:
            print(f"Недостаточно {selected_product.name}. Доступно: {selected_product.count}.")
        else:
            print(f"Вы купили {quantity} {selected_product.name}.")
            db.change_data_product_by_id_v2(selected_product.idCustomer, selected_product.count - quantity)
            selected_product.count -= quantity
    else:
        print("Неверный номер продукта.")


def addCustomer(db):
    firstname = input("Введите имя клиента: ")
    lastname = input("Введите фамилию клиента: ")
    phone = input("Введите номер телефона клиента: ")
    db.insert_data_client_by_id([firstname, lastname, phone])


def addProduct(db):
    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    count = int(input("Введите количество: "))
    id_category = int(input("Введите ID категории: "))
    id_customer = None  # Пока пропускаем ID клиента
    db.insert_data_product_by_id([price, name, count, id_category, id_customer])


def secondaryMenu(all_products):
    choice = -1
    while choice != 0:
        secondaryMenuView()
        choice = int(input())
        match choice:
            case 1:
                viewAllProducts(all_products)
            case 2:
                viewAllProductsByCategory(all_products)
            case 3:
                viewAllProducts_price(all_products)
            case 4:
                viewAllProducts_name(all_products)