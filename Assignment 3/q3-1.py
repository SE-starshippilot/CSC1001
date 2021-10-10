class Flower:
    def __init__(self):
        self.__name = 'Generic Flower'
        self.__num_of_petals = 4
        self.__price = 1.0

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print('This is not a valid name.')

    def set_num_of_petals(self, petal_num):
        if isinstance(petal_num, int) and petal_num > 0:
            self.__num_of_petals = petal_num
        else:
            print('This is not a valid petal number')

    def set_price(self, price):
        try:
            price = float(price)
            if price <= 0:
                raise Exception
        except Exception:
            print('This is not a valid price')
        else:
            self.__price = price

    def get_name(self):
        return self.__name

    def get_num_of_petals(self):
        return self.__num_of_petals

    def get_price(self):
        return self.__price
