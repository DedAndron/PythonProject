class User:
    def __truediv__(self, other):
        pass
    def __floordiv__(self, other):
        pass
    def __mod__(self, other):
        pass
    def __pow__(self, other):
        pass
    def __lt__(self, other):
        if isinstance(other, User):
            return self.__age<other.__age
        else:
            return None
    def __le__(self, other):
        pass
    def __gt__(self, other):
        pass
    def __ge__(self, other):
        pass
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass