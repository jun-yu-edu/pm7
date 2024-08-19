# 사용자가 자판기를 사용합니다.

class Person:

    def __init__(self, money):
        self.money = money

    def use(self, tool):
        tool.run(self)


class Beverages:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class VendingMachine:

    def __init__(self, beverages):
        self.beverages = beverages

    def show_menus(self):
        for beverage in self.beverages:
            if beverage.stock == 0:
                print('재고가 없습니다~~~')
            print(f'{beverage.name} : {beverage.price}원')

    def run(self, person):
        # 자판기가 실행됨

        # 메뉴의 이름과 가격을 보여준다.
        self.show_menus()

        # 돈을 받는다
        print(person.money)
        self.take_money(person)/
        # 메뉴를 선택한다
        self.choose_menu(person)
        # 돈이 충분한지 판단하고 
        # ....등등

cider = Beverages('사이다', 1400, 3)
coke = Beverages('콜라', 1500, 4)
water = Beverages('생수', 900, 1)

vending_machine = VendingMachine([cider, coke, water])
jun = Person(10000)


jun.use(vending_machine)
vending_machine.run(jun)
# jun.use(computer)
# jun.use(calculator)

dic = "{
    "price" : 1300,
    "stock" : 3
}"

