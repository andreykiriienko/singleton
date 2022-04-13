

class Singleton:
    _instances = None

    def __new__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super(Singleton, cls).__new__(cls)
        return cls._instances


if __name__ == '__main__':

    a = Singleton()
    b = Singleton()

    if id(a) == id(b):
        print('Шото получилось')
    else:
        print('Шото пошло не так')
