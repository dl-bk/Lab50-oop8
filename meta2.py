class MyMeta(type):
    def __new__(cls, name, bases, dct):
        required_attrs = ['attr1', 'attr2']
        for i in required_attrs:
            if i not in dct:
                raise AttributeError(f"In class must be [attr1, attr2] attributes")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass= MyMeta):
    attr1 = 10
    attr2 = 100


obj = MyClass()
print(obj.attr2)