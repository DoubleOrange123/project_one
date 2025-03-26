class Product:
    def __init__(self, price, name, is_new, count, id_category, id_customer):
        self.price = price
        self.name = name
        self.isNew = is_new
        self.count = count
        self.idCategory = id_category
        self.idCustomer = id_customer

    def __str__(self):
        return f"{self.name}, Цена: {self.price}, Количество: {self.count}"