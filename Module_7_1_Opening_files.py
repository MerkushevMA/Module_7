from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    __file_name = 'products.txt'
    file = open(__file_name, 'w')
    file.close()


    def get_products(self):
        file = open(self.__file_name, 'r')
        a = file.read()
        file.close()
        return a

    def add(self, *products):
        file2 = open(self.__file_name, 'a')
        #self.my_file = ""
        self.my_file = self.get_products()
        self.products = products
        for i in range(len(self.products)):
            self.find_string = self.products[i].name
            if self.my_file.upper().find(self.find_string.upper()) >= 0:
                print(f'Продукт {self.products[i]} уже есть в магазине.')
            else:
                file2.write(str(self.products[i]) + '\n')
        file2.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetable')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)

s1.add(p1, p2, p3)
s1.add(p1, p2, p3)

print(s1.get_products())
