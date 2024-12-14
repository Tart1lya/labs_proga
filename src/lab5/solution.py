import re

# Функция для проверки правильности номера телефона
def is_valid_phone(phone):
    return bool(re.match(r"^\+?\d{1}-\d{3}-\d{3}-\d{2}-\d{2}$", phone))

# Функция для проверки правильности адреса доставки
def is_valid_address(address):
    return bool(address) and bool(re.match(r"^.+\. .+\..+\. .+$", address))

# Функция для обработки и валидации заказов
def process_orders(file_path):
    valid_orders = []  # Список валидных заказов
    invalid_orders = []  # Список невалидных заказов

    # Открываем файл для чтения
    with open(file_path, 'r') as file:
        for line in file:
            # Разделение строки по разделителю ";"
            order = line.strip().split(';')

            # Проверяем, что строка имеет 6 элементов
            if len(order) != 6:
                continue  # Пропускаем строки с неправильным количеством данных

            # Разделяем строку на компоненты
            order_id = order[0]  # Идентификатор заказа
            products = order[1].split(', ')  # Список товаров
            customer_name = order[2]  # Имя клиента
            address = order[3]  # Адрес доставки
            phone = order[4]  # Номер телефона
            priority = order[5]  # Приоритет заказа

            # Проверка валидности адреса и телефона
            if not is_valid_address(address):
                invalid_orders.append(f"{order_id};1;{address if address else 'no data'}")
            if not is_valid_phone(phone):
                invalid_orders.append(f"{order_id};2;{phone if phone else 'no data'}")

            # Если заказ валиден, добавляем его в список валидных заказов
            if is_valid_address(address) and is_valid_phone(phone):
                # Подсчитываем количество каждого товара
                product_counts = {}
                for product in products:
                    product_counts[product] = product_counts.get(product, 0) + 1
                # Форматируем список товаров
                formatted_products = ', '.join([f"{product} x{count}" for product, count in product_counts.items()])

                # Добавляем заказ в список валидных заказов
                valid_orders.append((order_id, formatted_products, customer_name, address, phone, priority))

    return valid_orders, invalid_orders

# Функция для сортировки и сохранения валидных заказов по странам и приоритету
def save_valid_orders(valid_orders):
    def country_sort_key(order):
        # Получаем страну из адреса
        country = order[3].split('.')[0].strip()
        if country == "Россия":
            return 0, order[5]  # Россия сортируется первой, далее по приоритету
        return 1, country, order[5]  # Остальные страны сортируются по алфавиту и приоритету

    # Сортируем валидные заказы по ключу
    valid_orders.sort(key=country_sort_key)

    # Записываем валидные заказы в файл "order_country.txt"
    with open("order_country.txt", "w") as file:
        for order in valid_orders:
            # Форматируем адрес перед записью в файл
            file.write(f"{order[0]};{order[1]};{order[2]};"
                       f"{order[3].split('.')[0]}. {order[3].split('.')[1]}. {order[3].split('.')[2]};"
                       f"{order[4]};{order[5]}\n")

# Функция для сохранения невалидных заказов в файл "non_valid_orders.txt"
def save_invalid_orders(invalid_orders):
    with open("non_valid_orders.txt", "w") as file:
        for invalid_order in invalid_orders:
            file.write(invalid_order + "\n")

def main():
    # Обрабатываем заказы из файла "orders.txt"
    valid_orders, invalid_orders = process_orders("orders.txt")

    # Сохраняем валидные и невалидные заказы в отдельные файлы
    save_valid_orders(valid_orders)
    save_invalid_orders(invalid_orders)

if __name__ == "__main__":
    main()
