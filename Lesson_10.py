# Есть магазин, продукт (товар), покупатель, корзина и список покупок - это все отдельные классы, атрибуты и методы которых нужно продумать
# самостоятельно для того чтобы реализовать логику ниже
# Часть 1. Спроектировать классы.
# Написать классы:
# Продукт - атрибуты: 14, пате, рисе, атоипу
# Магазин - список продуктов (объектов класса Ргодис®)
# Покупатель - 14, количество денег, список продуктов (названия: молоко, сыр и тд), которые нужно купить - все задается при инициализации
# покупателя
# Корзина - 4, список продуктов (объектов класса Ргодис - по умолчанию Мопе)
# Часть 2. Написать бизнес-логику
# Реализовать следующие возможности:
# 1. Создается покупатель с определенным количеством денег и списком продуктов
# 2. Покупатель приходит в магазин и берет корзину (покупателю при помощи метода создается и добавляется корзина)
# 3. Создать экземпляр магазина, который должен быть синглтоном, в котором будет список продуктов
# 4. Покупатель проходится по списку продуктов, которые ему нужно купить и смотрит, есть ли в магазине эти продукты, если продукт есть, то
# покупатель добавляет его в свою корзину (нужен метод для добавления продукта РгоФиси в корзину) ТОЛЬКО ПРИ УСЛОВИИ что у покупателя
# достаточно денег. В ином случае вывести сообщение. Если денег достаточно, то. покупатель добавляет продукт в корзину и количество этого
# продукта в магазине уменьшается на 1
# 5. После того как прошлись по всем продуктам, вывести сообщение о том, какие продукты были куплены, а какие не были
import random


class Shop:

    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Shop, cls).__new__(cls)
        return cls.instance

    def __init__(self, list_products=None):
        self._list = list_products or self._list

    def check_products_in_shop(self):
        for item in self._list:
            return f'{item.amount} единиц {item.product_name} осталось'


class Product:

    def __init__(self, product_id, product_name, product_price, product_amount):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_amount = product_amount

    def give_info(self):
        return f'в магазине осталось {self.product_amount} единиц {self.product_name}'

    @staticmethod
    def show_info():
        requested_data = list()
        for element in Product:
            requested_data.append(element.give.info())
        return requested_data


class Bascet:

    def __init__(self, basket_id=None, goods=None):
        self.basket_id = basket_id
        self.goods = goods

    @property
    def basket_id(self):
        return self._basket_id

    @basket_id.setter
    def basket_id(self, basket_id):
        if basket_id is None:
            self.basket_id = random.randint(100, 200)


class Shopper:

    def __init__(self, shopper_id, money, shopping_list):
        self.shopper_id = shopper_id
        self.money = money
        self.shopping_list = shopping_list

    def give_basket(self, basket):
        self.basket = basket

    def add_to_basket(self):
        self._pay_with_cache()

    def __pay(self, unit):
        self.basket.goods = set()
        left_products = set()
        for element in self.shopping_list:
            for product in products:
                if element == product.products_name:
                    if unit >= product.price and product.amount > 0:
                        self.basket.goods.add(product.product_name)
                        product.amount -= 1
                        unit -= product.price
                    else:
                        left_products.add(product.product_name)
        if left_products:
            print(f'Недостаточно денег для {left_products}.')
        print(f'Добавил в корзину {self.basket.goods}')

    def __pay_witch_cache(self):
        self.__pay(self.money)

    def __buy_else(self, unit):
        more_products = set()
        for product in products:
            if unit >= product.price and product.amount > 0:
                self.basket.goods.add(product.product_name)
                product.amount -= 1
                unit -= product.price
                more_products.add(product.product_name)
        print(f'Добавленно {more_products}.')
        print(f'Денег осталось: {self.money}. В корзине сейчас: {self.basket.goods}')

    def show_money_left(self):
        return f'{self.shopper_id} осталось {self.money} денег'

    def exit_shoppint(self):
        self.basket = None


lemon = Product(product_id='1001', product_name='Lemon', product_price=6, product_amount=10),
apple = Product(product_id="1002", product_name='Apple', product_price=3, product_amount=10),
milk = Product(product_id="1003", product_name='Hilk', product_price=4, product_amount=10),
orange = Product(product_id="1004", product_name='Orange', product_price=7, product_amount=10),
cookie = Product(product_id="1005", product_name='Cookie', product_price=1, product_amount=10)
