# Створіть метаклас, який автоматично реєструє всі
# нові класи у певному реєстрі для подальшого
# використання.

class Meta(type):
    registry = {}

    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        cls.registry[name] = new_cls

        return new_cls


class Cls1(metaclass=Meta):
    pass

class Cls2(metaclass=Meta):
    pass

obj1 = Cls1()
obj2 = Cls2()

print(Meta.registry)