# Реалізуйте метаклас, що забороняє спадкування від
# певних класів чи змінює порядок спадкування.

class SomeMeta(type):
    def __new__(cls, name, bases, dct):
        try:
            forbidden_classes = dct['forbidden_classes']
            for forbid_cls in forbidden_classes:
                if forbid_cls in bases:
                    raise TypeError(f'Inheritance from {forbid_cls.__name__} is not allowed.')
        except KeyError:
            pass
        
        return super().__new__(cls, name, bases, dct)

class Allowed:
    pass

class Forbidden:
    _b = 19
    pass

class SomeClass(Allowed, Forbidden, metaclass=SomeMeta):
    forbidden_classes = [Forbidden]

    a = 10


obj = SomeClass()


