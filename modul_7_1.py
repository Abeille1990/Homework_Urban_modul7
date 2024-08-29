from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:

    def __init__(self):
        self.__file_name = 'product.txt'

    def get_products(self):
        with open('product.txt','r') as file:
            # file.seek(0)
            data = ''.join(file.readlines())
            return data

        # file = open(self.__file_name,'r')
        # print(''.join(file.readlines()))


    def add(self, *products):

        shop_products = self.get_products()

        for product in products:
            if product.name in shop_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name,'a')
                file.write(f'\n{product}')
                file = open(self.__file_name, 'r')
                pprint(file.read())
                file.close()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1 = Shop()

print(p2)

s1.add(p1,p2,p3)

print(s1.get_products())
