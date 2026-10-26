class MyMeta(type):
    #mcls - ссылка на наш класс
    #name - название
    #bases - кортеж (родительские классы)
    #attrs - dict {name: "Alex", say_hi:lambda self:'hello, self.name'}
    def __new__(mcls, name, bases, attrs):
        print(f'Сделался класс {name}')
        attrs['category'] = 'general'
        return super().__new__(mcls,name,bases,attrs)
class Product(metaclass=MyMeta):
    pass
class Person(metaclass=MyMeta):
    pass
pr = Product()
print(pr.category)