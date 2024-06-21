import csv
from datetime import datetime, date

class Person:
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        
        # Перетворення рядка у об'єкт datetime.date
        year, month, day = map(int, birth_date.split('-'))
        self.birth_date = date(year, month, day)
    
    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return str(age)
    
    def get_fullname(self):
        return f"{self.surname} {self.first_name}"

def modifier(filename):
    try:
        # Прочитати дані з файлу
        with open(filename, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            data = list(reader)
        
        # Визначити нові заголовки
        fieldnames = reader.fieldnames[:2] + ['fullname'] + reader.fieldnames[2:] + ['age']
        
        # Створити об'єкти класу Person та модифікувати дані
        modified_data = []
        for row in data:
            person = Person(
                surname=row['surname'],
                first_name=row['first_name'],
                birth_date=row['birth_date'],
                nickname=row.get('nickname')
            )
            row['fullname'] = person.get_fullname()
            row['age'] = person.get_age()
            modified_data.append(row)
        
        # Записати модифіковані дані в новий файл
        output_filename = 'modified_' + filename
        with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(modified_data)
        
        print(f"Modified file saved as {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Приклад використання функції
modifier('contacts.csv')
