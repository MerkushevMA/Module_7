from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    __file__name = 'products.txt'
    file = open(__file__name, 'w')
    file.close()
    print(file)

    def get_products(self):
        file = open(self.__file__name, 'r')
        file.read()
        pprint(file.read())
        file.close()

    def add(self, *products):
        file = open(self.__file__name, 'r')
        content = file.read()
        if str(products) in content:
            print(f'Продукт {products} уже есть в магазине')
            file.close()
        else:
            file.close()
            file = open(self.__file__name, 'a')
            file.write(str(products))
            file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetable')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)

s1.add(p1, p2, p3)