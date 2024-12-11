import re

# Функция для проверки правильности номера телефона
def is_valid_phone(phone):
    return bool(re.match(r"^\+?\d{1}-\d{3}-\d{3}-\d{2}-\d{2}$", phone))

# Функция для проверки правильности адреса доставки
def is_valid_address(address):
    return bool(address) and bool(re.match(r"^.+\. .+\..+\. .+$", address))

# Функция для обработки и валидации заказов
def process_orders(file_path):
    valid_orders = []
    invalid_orders = []

    with open(file_path, 'r') as file:
        for line in file:
            # Пропускаем пустые строки
            if not line.strip():
                continue

            # Разделение строки по разделителю
            order = line.strip().split(';')

            # Проверяем, что строка имеет 6 элементов
            if len(order) != 6:
                continue  # Пропускаем строки с неправильным количеством данных

            # Разделяем строку на компоненты
            order_id = order[0]
            products = order[1].split(', ')
            customer_name = order[2]
            address = order[3]
            phone = order[4]
            priority = order[5]

            # Проверка ошибок
            if not is_valid_address(address):
                invalid_orders.append(f"{order_id};1;{address if address else 'no data'}")
            if not is_valid_phone(phone):
                invalid_orders.append(f"{order_id};2;{phone if phone else 'no data'}")

            # Если заказ без ошибок, сохраняем
            if is_valid_address(address) and is_valid_phone(phone):
                # Форматирование продуктов
                product_counts = {}
                for product in products:
                    product_counts[product] = product_counts.get(product, 0) + 1
                formatted_products = ', '.join([f"{product} x{count}" for product, count in product_counts.items()])

                # Добавляем заказ в список валидных заказов
                valid_orders.append((order_id, formatted_products, customer_name, address, phone, priority))

    return valid_orders, invalid_orders


# Функция для сортировки заказов по стране и приоритету
def save_valid_orders(valid_orders):
    def country_sort_key(order):
        # Разделение адреса на компоненты и сортировка по стране
        country = order[3].split('.')[0].strip()
        if country == "Россия":
            return (0, order[5])  # "Российская Федерация" на первом месте
        return (1, country, order[5])  # Для остальных стран сортируем по алфавиту и приоритету

    # Сортируем по ключу, учитывая страну и приоритет
    valid_orders.sort(key=country_sort_key)

    with open("order_country.txt", "w") as file:
        for order in valid_orders:
            # Записываем заказ в файл с форматированием адреса
            file.write(f"{order[0]};{order[1]};{order[2]};{order[3].split('.')[0]}. {order[3].split('.')[1]}. {order[3].split('.')[2]};{order[4]};{order[5]}\n")


# Функция для записи невалидных заказов в файл
def save_invalid_orders(invalid_orders):
    with open("non_valid_orders.txt", "w") as file:
        for invalid_order in invalid_orders:
            file.write(invalid_order + "\n")


# Основная функция
def main():
    valid_orders, invalid_orders = process_orders("orders.txt")

    save_valid_orders(valid_orders)
    save_invalid_orders(invalid_orders)


if __name__ == "__main__":
    main()
