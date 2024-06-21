import csv

# Приклад даних для контакту
data = [
    {"surname": "Doe", "first_name": "John", "birth_date": "2002-12-31", "nickname": "Johnny"},
    {"surname": "Smith", "first_name": "Jane", "birth_date": "1990-05-15", "nickname": "Janey"},
    {"surname": "Brown", "first_name": "Bob", "birth_date": "1985-07-23", "nickname": ""},
    {"surname": "White", "first_name": "Alice", "birth_date": "1999-11-09", "nickname": "Aly"},
]

# Заголовки колонок
fieldnames = ["surname", "first_name", "birth_date", "nickname"]

# Створення файлу contacts.csv
with open('contacts.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("contacts.csv створено успішно")
