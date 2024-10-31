# Задание 2

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Product:
    def __init__(self, name, quantity, price):
        self.name = name  # Название товара
        self.quantity = quantity  # Количество товара
        self.price = price  # Цена товара за единицу

    def increase_quantity(self, amount):
        self.quantity += amount
        logging.info(f"Увеличено количество товара '{self.name}' на {amount}. Текущее количество: {self.quantity}")

    def decrease_quantity(self, amount):
        if amount > self.quantity:
            logging.info(f"Попытка уменьшить количество товара на {amount} при наличии {self.quantity}")
            raise ValueError(f"Недостаточно товара '{self.name}'")
        self.quantity -= amount
        logging.info(f"Уменьшено количество товара '{self.name}' на {amount}. Текущее количество: {self.quantity}")

    def calculate_price(self):
        return self.quantity * self.price


class Warehouse:
    '''Склад товаров'''
    def __init__(self):
        self.products = {}  # Словарь товаров: ключ - название товара, значение - объект Product

    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name].increase_quantity(product.quantity)
        else:
            self.products[product.name] = product
            logging.info(f"Добавлен новый товар '{product.name}' на склад")

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            logging.info(f"Товар '{product_name}' удален со склада")
        else:
            raise ValueError(f"Товар '{product_name}' не найден на складе")

    def calculate_total_value(self):
        total_value = sum(product.calculate_price() for product in self.products.values())
        logging.info(f"Рассчитана общая стоимость товаров на складе: {total_value}")
        return total_value


class Seller:
    def __init__(self, name):
        self.name = name
        self.sales_report = []  # Список для хранения информации о продажах

    def sell_product(self, warehouse, product_name, quantity):
        if product_name not in warehouse.products:
            raise ValueError(f"Товар '{product_name}' не найден на складе")
        product = warehouse.products[product_name]
        product.decrease_quantity(quantity)
        if product.quantity == 0:
            warehouse.remove_product(product_name)
            logging.info(f"Товар {product_name} удален со скалада, потому что закончился")
        sale_amount = quantity * product.price
        self.sales_report.append({
            "product_name": product_name,
            "quantity": quantity,
            "sale_amount": sale_amount
        })
        logging.info(f"{self.name} продал {quantity} ед. '{product_name}' на сумму {sale_amount}")
        return sale_amount

    def generate_sales_report(self):
        total_sales = sum(sale["sale_amount"] for sale in self.sales_report)
        report = f"Отчет о продажах продавца {self.name}:\n"
        for sale in self.sales_report:
            report += f"{sale['product_name']} - {sale['quantity']} ед. - на сумму {sale['sale_amount']}\n"
        report += f"Общая выручка: {total_sales}"
        logging.info("Сформирован отчет о продажах")
        return report

# Пример использования
# Создание товаров
product1 = Product("Джинсы", 50, 10000)
product2 = Product("Футболка", 100, 3000)
product3 = Product("Носки", 30, 1000)

# Создание склада и добавление товаров
warehouse = Warehouse()
warehouse.add_product(product1)
warehouse.add_product(product2)

# Создание продавца и продажа товаров
seller = Seller("Иван")
seller.sell_product(warehouse, "Джинсы", 50)
seller.sell_product(warehouse, "Футболка", 20)

# Отчет о продажах
print(seller.generate_sales_report())

# Подсчет общей стоимости товаров на складе
print("Общая стоимость товаров на складе:", warehouse.calculate_total_value())
