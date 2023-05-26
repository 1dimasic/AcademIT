class Contact:
    def __init__(self, surname, name, telephone_number):
        self.__surname = surname
        self.__name = name
        self.__telephone_number = telephone_number

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def telephone_number(self):
        return self.__telephone_number

    @telephone_number.setter
    def telephone_number(self, telephone_number):
        self.__telephone_number = telephone_number


# Создаем два новых объекта экземпляра класса Contact
bob = Contact('Smith', 'Bob', '85-560')
sue = Contact('Jones', 'Sue', '96-381')

# Изменяем значение атрибута экземпляра
bob.telephone_number = '00-025'
bob.name = 'Boby'
print(bob.surname, bob.name, bob.telephone_number)

# Изменяем значение атрибута экземпляра
sue.surname = 'Wood'
sue.telephone_number = '99-328'
print(sue.surname, sue.name, sue.telephone_number)
