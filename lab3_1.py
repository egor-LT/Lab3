from datetime import datetime, date

class Person:
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        # Перетворення рядка у дату
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

# Приклад використання
person = Person(surname="Lytvyn", first_name="Egor", birth_date="2005-01-27")
print(person.get_fullname())  
print(person.get_age())       
