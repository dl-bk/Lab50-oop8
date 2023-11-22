class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct["smth"] = lambda self: print(f"method from {self.__class__.__name__}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass= MyMeta):
    pass

obj = MyClass()
obj.smth()