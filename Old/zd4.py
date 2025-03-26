class animal():
    def __init__(self, name='Karl', age=2, voice='') -> None:
        self.name = name
        self.age = age
        self.voice = voice

    def __str__(self) -> str:
        return f'Name: {self.name}, voice: {self.voice}'
    
    def jump(self) -> None:
        print(f'{self.name} сделаль прыжок')

class dog(animal):
    def __init__(self, name='Karl', age=2, voice='', ass = True) -> None:
        super().__init__(name, age, voice)
        self.ass = ass

    def __str__(self) -> str:
        return super().__str__() + f', ass: {self.ass}'

class cat(animal):
    def __init__(self, name='Karl', age=2, voice='meow-meow') -> None:
        super().__init__(name, age, voice)


d = dog(voice='gaf-gaf')
c = cat('Kitty')
d.jump()
c.jump()
print(d)
print(c)