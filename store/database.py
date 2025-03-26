class database:
    def open_connections(self):
        # Заглушка для подключения к базе данных
        print("Подключение к базе данных выполнено.")

    def select_all_products(self):
        # Возвращаем имитацию данных из базы
        print("Получение всех продуктов из базы...")
        return [
            [100, "Laptop", True, 10, 1, 1],
            [50, "Phone", True, 20, 2, 2],
        ]

    def insert_data_client_by_id(self, client_data):
        print(f"Клиент добавлен: {client_data}")

    def insert_data_product_by_id(self, product_data):
        print(f"Продукт добавлен: {product_data}")

    def change_data_product_by_id_v2(self, product_id, new_count):
        print(f"Количество продукта {product_id} обновлено: {new_count}")