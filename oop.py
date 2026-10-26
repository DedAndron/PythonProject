# class Person:
#     __counter = 0
#     def __init__(self, name, surname, dateofbirth, phonenum, sity, country, address):
#         Person.__counter += 1
#         self.__name = name
#         self.__surname = surname
#         self.__dob = dateofbirth
#         self.__phonenum = phonenum
#         self.__sity = sity
#         self.__country = country
#         self.__address = address
#
#     @property
#     def name(self):
#         return self.__name
#     def surname(self):
#         return self.__surname
#     def dob(self):
#         return self.__dob
#     def phonenum(self):
#         return self.__phonenum
#     def sity(self):
#         return self.__sity
#     def country(self):
#         return self.__country
#     def address(self):
#         return self.__address
#
#     @name.setter
#     def name(self, name):
#         if type(name) is not str:
#             raise TypeError("name must be a string")
#         if name == "":
#             raise ValueError("name cannot be an empty string")
#         self.__name = name
#     @surname.setter
#     def surname(self, surname):
#         if type(surname) is not str:
#             raise TypeError("surname must be a string")
#         if surname == "":
#             raise ValueError("surname cannot be an empty string")
#         self.__surname = surname
#     @dob.setter
#     def dob(self, dateofbirth):
#         self.__dateofbirth = dateofbirth
#     @phonenum.setter
#     def phonenum(self, phonenum):
#         self.__phonenum = phonenum
#     @sity.setter
#     def sity(self, sity):
#         self.__sity = sity
#     @country.setter
#     def country(self, country):
#         self.__country = country
#     @address.setter
#     def address(self, address):
#         self.__address = address
#
#     def __str__(self):
#         return (f'Name: {self.__name}'
#                 f'Surname: {self.__surname}'
#                 f'Data of birthday: {self.__dob}'
#                 f'Phone number: {self.__phonenum}'
#                 f'Sity: {self.__sity}'
#                 f'Country: {self.__country}'
#                 f'Address: {self.__address}')
#     def show_person(self):
#         print (f'Name: {self.__name}\nSurname: {self.__surname}\nData of birthday: {self.__dob}\nPhone number: {self.__phonenum}\nSity: {self.__sity}\nCountry: {self.__country}\nAddress: {self.__address}')
#
# person = Person('Nick','Woterson', '25.05.1985', '888-8888-88-88', 'London', 'UK', 'str.Nevada 13')
# print(person.show_person())
# type(
#     "Player",
#     (),
#     {
#         'role':'super admin',
#         'age':20,
#         'move':lambda self:f'Moving...()'
#     }
# )
from User import *

us1 = User("Bogdan", 20)
us2 = User("Ivan", 30)
if us1<us2:
    print(us1)
else:
    print(us2)

