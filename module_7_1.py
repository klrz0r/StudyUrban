class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name,'r')
        text = file.read()
        file.close()
        return text

    def add(self, *products: Product):
        file = open(self.__file_name, 'a')
        text_file = self.get_products()
        for product in products:
            product_str = product.name + ', ' + str(product.weight) + ', ' + product.category
            if not (product_str in text_file):
                file.write(f'{product_str}\n')
            else:
                print(f'Продукт {product_str} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


