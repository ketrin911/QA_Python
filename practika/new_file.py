# def test_abs1():
#     assert abs (-42) == 42, 'shoud be absolute value of a number'

# def test_abs2():
#     assert abs(-42) == -42, 'Should be absolute value of a number'

# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print('all test passed!')

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f'{self.name} say ГАВ ГАВ ГАВ'
   
class Cat(Animal):
    def speak(self):
        return f"{self.name} say МЯУ ГДЕ ЕДА "
   
dog = Dog('Гром')
cat = Cat('Йота')

print(dog.speak())
print(cat.speak())
