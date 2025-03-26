from database import database
from classes import product
from views import menu, secondaryMenu, ThirdMenu, addCustomer, addProduct

def main():
    # Создание подключения к базе данных
    db = database()

    # Получение всех продуктов из базы данных
    all_products = db.select_all_products()
    all_products = convert(all_products)  # Конвертация в объекты класса "product"

    # Главное меню
    choice = -1
    while choice != 0:
        menu()  # Отображаем меню
        choice = int(input("Введите номер опции: "))
        match choice:
            case 1:
                addCustomer(db)
            case 2:
                addProduct(db)
            case 3:
                secondaryMenu(all_products)  # Отправляем список продуктов в меню
            case 4:
                ThirdMenu(all_products, db)  # Покупка продукта
            case 0:
                print("Программа завершена. Спасибо за использование!")
                break


def convert(products):
    """Конвертирует список данных из базы данных в список объектов класса Product"""
    converted_data = []
    for prod in products:
        converted_data.append(product(*prod))
    return converted_data


if __name__ == "__main__":
    main()