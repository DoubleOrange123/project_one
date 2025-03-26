1. # Реализовать класс Стол с 4 полями
class table:
    def __init__(self, width = 5) -> None:
        self.width = width
        self.length = 20
        self.colour = 'red'
        self.material = 'stone'
t = table ()
t2 = table (15)
t3 = table (40)
print(t.width, t.length, t.colour, t.material)
print(t2.width, t2.length, t2.colour, t2.material)
print(t3.width, t3.length, t3.colour, t3.material)
l = [t, t2, t3]
for i in range(len(l)):
    if l[i].width > 20:
        print (l[i].width)
    
    


