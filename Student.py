class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def test1(self):
        print(self)
        print("test1")

    @classmethod
    def from_string(cls, serialize_object):
        obj = serialize_object.spit(":")
        return cls(obj[0], obj[1])

    @staticmethod
    def test3():
        pass
