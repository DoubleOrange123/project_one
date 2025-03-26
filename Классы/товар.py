class goods:
    def __init__(self, name, category, price, units) -> None:
        self.name = name
        self.category = category
        self.price = price
        self.units = units
    def info(self):
        print(self.name, self.category, self.price, self.units)
    def buy(self,money):
        if money >= self.price: 
            self.units = self.units - 1
            print('продано')
        else: 
            print('нет деняк')

s1 = goods('Шорты', 'apparel', 200, 5)
s2 = goods('Футболки', 'apparel', 300, 7)
s2.name = 'Футболки'
s2.category = 'apparel'
s2.price = 400
s2.units = 7
s2.info()
s1.info()
s1.buy(2)
s1.info()

        
    