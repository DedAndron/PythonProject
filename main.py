import json
from datetime import date
from Book import Book
from Student import *
# from abc import ABC, abstractmethod
#
# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
# class Car(Transport):
#     def move(self):
#         print("Car moved")
#
# class Bus(Transport):
#     def move(self):
#         print("Bus moved")
#
# def drive(tr):
#     if isinstance(tr, Transport):
#         tr.move()
#
# class Document(ABC):
#     def __init__(self, title, text, ext, pages):
#         self.title = title
#         self.text = text
#         self.ext = ext
#         self.pages = pages
#
#     @abstractmethod
#     def get_document_info(self):
#         pass
#
# class ExcellDocument(Document):
#     def get_document_info(self):
#         return {"title": self.title,
#                 "text": self.text,
#                 "ext": self.ext,
#                 "pages": self.pages}
#
# class WordDocument(Document):
#     def get_document_info(self):
#         return {"title": self.title,
#                 "text": self.text,
#                 "ext": self.ext,
#                 "pages": self.pages}
# class HtmlDocument(Document):
#     def get_document_info(self):
#         return {"title": self.title,
#                 "text": self.text,
#                 "ext": self.ext,
#                 "pages": self.pages}
# class Printer():
#     def __init__(self, model):
#         self.model = model
#     def print_document(self, document):
#         print(f"Printer: {self.model}")
#         print("Start printing...")
#         print(document.get_document_info())
#         print("End printing...")

# class JsonSerializerMixin:
#     def to_json(self):
#         return json.dumps(self.__dict__, default=str, ensure_ascii=False)
#
# class TimeMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         from datetime import datetime
#         self.created_at = datetime.now()
#
# class User(JsonSerializerMixin, TimeMixin):
#     def __init__(self, username: str):
#         super().__init__()
#         self.username = username
# class LoggingMixin:
#     def log(self, message):
#         print(f"[LOG] {message}")
# class User(LoggingMixin):
#     def __init__(self, name):
#         self.name = name
#
#     def login(self):
#         self.log(f"{self.name} увійшов у систему")
# class Group:
#     i = 0
#     def __init__(self, students=None):
#         self._students = students
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.i==len(self._students):
#             raise StopIteration
#         return self._students[self.i]

def main():
    book1 = Book('Title1','Author1',2024,457)
    book2 = Book('Title2','Author2',2024,367)
    book3 = Book('Title3','Author3',2028,-2)
    print(book1.__str__())
    print(book2.__str__())
    print(book3.__str__())
    print()
    print(book1.__repr__())
    print(book2.__repr__())
    print()
    print(book1.__len__())
    print(book2.__len__())
    print()
    print(book1.__eq__(book2))
    print()
    print(book1.__lt__(book2))
    print()
    print(book1.__add__(book2))
    print()
    print(book1.__contains__('Title'))
    print(book2.__contains__('Name'))
    # group = Group(['Alex', 'Bob', 'Egor'])
    # for student in group:
    #     print(student)
    # user = User("Alex")
    # user.login()
    # printer = Printer("HP")
    # document1 = ExcellDocument(
    #     "Звіт",
    #     "Звіт про продажі за місяць",
    #     ".xlsx",
    #     5
    # )
    #
    # document2 = WordDocument(
    #     "Реферат",
    #     "Реферат з інформатики",
    #     ".docx",
    #     10
    # )
    #
    # document3 = HtmlDocument(
    #     "Вебсторінка",
    #     "Моя перша HTML-сторінка",
    #     ".html",
    #     1
    # )
    # printer.print_document(document1)
    # printer.print_document(document2)
    # printer.print_document(document3)
    # drive(Car())
    # drive(Bus())
    # s = Student()
    # s.test1()
    # Student.test2()
    # set = {2,3,4,5,2,5}
    # set1 = {1,2,3,4,5}
    # set2 = {2,3,4,5,6,7}
    # union = set1.union(set2)
    # intersection = set1.intersection(set2)
    # print(set,union,intersection)
    # fructs = ("apple", "banana", "cherry", "grape", "mango", "apple", "cherry", "mango", "pineapple")
    # us_input = input("What are you looking for? ")
    # print(fructs.count(us_input))
    # cardevelopers = ["BMW","Volkswagen","Toyota","Lada"]
    # dev_name = input("Enter developer name: ")
    # new_name = input("Enter new developer name: ")
    # for i in range(len(cardevelopers)):
    #     if cardevelopers[i] == dev_name:
    #         cardevelopers[i] = new_name
    #     else:
    #         print("Developer Name Error")
    # print (cardevelopers)
    # get_sum = lambda x, y: x + y
    # print(type((4,5)))
if __name__ == '__main__':
    main()