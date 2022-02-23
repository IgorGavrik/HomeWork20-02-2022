# # 11.01 Создать пустой класс Dog
# class dog:
#     """Базовый класс для всех собак - Dog"""
#     def __init__(self, breed, color, height, weight):
#         self.breed = breed
#         self.color = color
#         self.height = height
#         self.weight = weight
#     def dog_description(self):
#         print(f'Breed: {self.breed}. Colour: {self.color}. Height: {self.height}. Weight: {self.weight}')
#     def dog_jump(self):
#         print(f'{self.breed} Jump!')
#     def dog_run(self):
#         print(f'{self.breed} Run!')
# # 11.02 Создать два объекта класса Dog. Вывести их на экран
# dog1 = dog("cocker", "black", 50, 35)
# dog2 = dog("fox", "grey", 45, 25)
# dog1.dog_description()
# dog2.dog_description()
# # 11.03 Добавить два метода в класс Dog: jump и run. Методы
# # выводят на экран Jump! и Run! соответственно.
# dog1.dog_run()
# dog2.dog_jump()


# # 11.04 Создать класс Dog. Класс имеет четыре
# # атрибута: height, weight, name, age. Класс
# # имеет три метода: jump, run, bark. Каждый
# # метод выводит сообщение на экран. Создать
# # объект класса Dog, вызвать все методы
# # объекта и вывести на экран все его атрибуты.
# class dog:
#     def __init__(self, height, weight, name, age, master, address):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#         self.__master = master
#         self.__address = address
#     def dog_description(self):
#         print(f'Height: {self.height}. Weight: {self.weight}. Name: {self.name}. Age: {self.age}.')
#     def dog_jump(self):
#         print(f'Jump!')
#     def dog_run(self):
#         print(f'Run!')
#     def dog_bark(self):
#         print(f'Bark!')
#     def dog_change_name(self, name):
#         self.name = name
#     def dog_name(self):
#         print(f'Dog name: {self.name}')
#     def get_master(self):
#         print(f'Dog master: {self.__master}')
#         # Так то же работает
#         # print(f'Dog master: {self._dog__master}')
#     def get_address(self):
#         return self.__address
#     def set_address(self,address):
#         self.__address = address
# dog_pet = dog(50, 35, 'Max', 15, 'Sam', 'Minsk')
# dog_pet.dog_jump()
# dog_pet.dog_run()
# dog_pet.dog_bark()
# dog_pet.dog_description()
# dog_pet.get_master()
# # # 11.05 Добавить в класс Dog метод change_name. Метод
# # # принимает на вход новое имя и меняет атрибут имени у
# # # объекта. Создать один объект класса. Вывести имя.
# # # Вызвать метод change_name. Вывести имя.
# dog_pet.dog_change_name('Mark')
# dog_pet.dog_name()
# dog_pet.dog_description()
# # Ссылка по описанию классов
# # https://pythonru.com/primery/primery-raboty-s-klassami-v-python
# # 11.06 Добавить в метод инициализации новый приватный
# # атрибут - master. Создать метод get_master() который
# # возвращает значение атрибута master.
# # Используй код выше: там уже определен приватный параметр и определён метод
# # Вывод значения атрибута ниже. Он не выводится в общем описании поскольку
# # является приватным
# dog_pet.get_master()
# # 11.07 Добавить новый приватный атрибут адрес(по-умолчанию
# # равен ‘Minsk’). Добавить getter и setter для адреса.
# # другой способ вывода (без метода)
# print(f'Dog address (private): {dog_pet._dog__address}')
# # Вывод адреса методом
# print(f'Dog address again: {dog_pet.get_address()}')
# dog_pet.set_address('Gomel')
# print(f'New dog address: {dog_pet.get_address()}')

# # декоратор @property позволяет обращаться к методам без использования скобок
# @property
# def get_master(self):
#     print(f'Dog master: {self.__master}')

# 11.08 Сделать все атрибуты класса Dog приватными. Сделать
# для каждого атрибута getter и setter используя
# декораторы. Все change методы удалить
# class Dog:
#     def __init__(self, height, weight, name, age, master, address):
#         self.__height = height
#         self.__weight = weight
#         self.__name = name
#         self.__age = age
#         self.__master = master
#         self.__address = address
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         self.__height = height
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.__weight = weight
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @property
#     def master(self):
#         return self.__master
#
#     @master.setter
#     def master(self, master):
#         self.__master = master
#
#     @property
#     def address(self):
#         return self.__address
#
#     @address.setter
#     def address(self, address):
#         self.__address = address
#
#
# dog_pet = Dog(50, 35, 'Max', 15, 'Sam Orwel', 'Minsk')
# print(f'Dog height given: {dog_pet.height}')
# dog_pet.height = 45
# print(f'Dog height changed: {dog_pet.height}')
# print(f'Dog weight given: {dog_pet.weight}')
# dog_pet.weight = 40
# print(f'Dog weight changed: {dog_pet.weight}')
# print(f'Dog name given: {dog_pet.name}')
# dog_pet.name = 'Black'
# print(f'Dog name changed: {dog_pet.name}')
# print(f'Dog age given: {dog_pet.age}')
# dog_pet.age = 8
# print(f'Dog age changed: {dog_pet.age}')
# print(f'Dog master given: {dog_pet.master}')
# dog_pet.master = 'Peter Simpson'
# print(f'Dog master changed: {dog_pet.master}')
# print(f'Dog address given: {dog_pet.address}')
# dog_pet.address = 'Gomel'
# print(f'Dog address changed: {dog_pet.address}')

# 11.09 Создать три класса: Dog, Cat, Parrot. Атрибуты каждого
# класса: name, age, master. Каждый класс содержит
# конструктор и методы: run, jump, birthday(увеличивает age
# на 1), sleep. Класс Parrot имеет дополнительный метод fly.
# Cat - meow, Dog - bark.
# class Dog:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def dog_jump(self):
#         return 'jump'
#
#     def dog_run(self):
#         return 'run'
#
#     def dog_sleep(self):
#         return 'sleep'
#
#     def dog_bark(self):
#         return 'bark'
#
# class Cat:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def cat_jump(self):
#         return 'jump'
#
#     def cat_run(self):
#         return 'run'
#
#     def cat_sleep(self):
#         return 'sleep'
#
#     def cat_meow(self):
#         return 'meow'
#
#
# class Parrot:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def parrot_jump(self):
#         return 'jump'
#
#     def parrot_run(self):
#         return 'run'
#
#     def parrot_sleep(self):
#         return 'sleep'
#
#     def parrot_fly(self):
#         return 'fly'
#
#
# dog_pet = Dog('Max', 8, 'Sam Orwel')
# cat_pet = Cat('Rich', 4.5, 'Igor Gavrik')
# parrot_pet = Parrot('Rick', 5, 'Lera Simpson')
# print(f'Dog name: {dog_pet.name}. Dog age: {dog_pet.age}. Dog master: {dog_pet.master}.')
# print(f'Cat name: {cat_pet.name}. Cat age: {cat_pet.age}. Cat master: {cat_pet.master}.')
# print(f'Parrot name: {parrot_pet.name}. Parrot age: {parrot_pet.age}. Parrot master: {parrot_pet.master}.')
# print(f'\nDog, Cat and Parrot have celebrated their Birthdays.')
# dog_pet.age = dog_pet.age + 1
# cat_pet.age = cat_pet.age + 1
# parrot_pet.age = parrot_pet.age + 1
# print(f'Dog age changed: {dog_pet.age}. Cat got older and now: {cat_pet.age}. Parrot followed them and went to: {parrot_pet.age}')
# print('')
# print(f'Dog {dog_pet.name} can {dog_pet.dog_jump()}, {dog_pet.dog_run()}, {dog_pet.dog_sleep()} and like no others - {dog_pet.dog_bark()}.')
# print(f'Cat {cat_pet.name} can {cat_pet.cat_jump()}, {cat_pet.cat_run()}, {cat_pet.cat_sleep()} and like no others - {cat_pet.cat_meow()}.')
# print(f'Parrot {parrot_pet.name} can {parrot_pet.parrot_jump()}, {parrot_pet.parrot_run()}, {parrot_pet.parrot_sleep()} and like no others - {parrot_pet.parrot_fly()}.')

# 11.10 Создать родительский класс Pet, содержащий все общие методы классов
# Dog, Cat, Parrot. Унаследовать Dog, Cat, Parrot от класса Pet. Удалить в
# дочерних классах те методы, которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы.
# class Pet:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     @property
#     def pet_jump(self):
#         return 'jump'
#
#     @property
#     def pet_run(self):
#         return 'run'
#
#     @property
#     def pet_sleep(self):
#         return 'sleep'
#
#
# class Dog(Pet):
#     def dog_bark(self):
#         return 'bark'
#
#
# class Cat(Pet):
#     def cat_meow(self):
#         return 'meow'
#
#
# class Parrot(Pet):
#     def parrot_fly(self):
#         return 'fly'
#
#
# dog_pet = Dog('Max', 8, 'Sam Orwel')
# cat_pet = Cat('Rich', 4.5, 'Igor Gavrik')
# parrot_pet = Parrot('Rick', 5, 'Lera Simpson')
# print(f'Dog name: {dog_pet.name}. Dog age: {dog_pet.age}. Dog master: {dog_pet.master}.')
# print(f'Cat name: {cat_pet.name}. Cat age: {cat_pet.age}. Cat master: {cat_pet.master}.')
# print(f'Parrot name: {parrot_pet.name}. Parrot age: {parrot_pet.age}. Parrot master: {parrot_pet.master}.')
# print(f'\nDog, Cat and Parrot have celebrated their Birthdays.')
# dog_pet.age = dog_pet.age + 1
# cat_pet.age = cat_pet.age + 1
# parrot_pet.age = parrot_pet.age + 1
# print(f'Dog age changed: {dog_pet.age}. Cat got older and now: {cat_pet.age}. Parrot followed them and went to: {parrot_pet.age}')
# print('')
# print(f'Dog {dog_pet.name} can {dog_pet.pet_jump}, {dog_pet.pet_run}, {dog_pet.pet_sleep} and like no others - {dog_pet.dog_bark()}.')
# print(f'Cat {cat_pet.name} can {cat_pet.pet_jump}, {cat_pet.pet_run}, {cat_pet.pet_sleep} and like no others - {cat_pet.cat_meow()}.')
# print(f'Parrot {parrot_pet.name} can {parrot_pet.pet_jump}, {parrot_pet.pet_run}, {parrot_pet.pet_sleep} and like no others - {parrot_pet.parrot_fly()}.')

# 11.11 Добавить два новых атрибута в родительский класс: weight и height.
# Добавить методы change_weight, change_height принимающий один
# параметр и прибавляющий его к соответствующему аргументу. В случае если
# параметр не был передан, увеличивать на 0.2.
# Изменить метод fly класса Parrot. Если вес больше 0.1 выводить сообщение
# This parrot cannot fly.
class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    @property
    def pet_jump(self):
        return 'jump'

    @property
    def pet_run(self):
        return 'run'

    @property
    def pet_sleep(self):
        return 'sleep'

    def weight(self):
        self.weight = weight

    @property
    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight = weight + 0.2

    def height(self):
        self.height = height

    def change_height(self, height):
        if height:
            self.height = height
        else:
            self.height += 0.2


class Dog(Pet):
    def dog_bark(self):
        return 'bark'


class Cat(Pet):
    def cat_meow(self):
        return 'meow'


class Parrot(Pet):
    @property
    def parrot_fly(self):
        return 'fly'

    def parrot_fly(self, weight):
        self.weight = weight
        if self.weight>0.1:
            fly = 'This parrot cannot fly'
        else:
            fly = 'This parrot can fly still'
        return fly


dog_pet = Dog('Max', 8, 'Sam Orwel', 15, 45)
cat_pet = Cat('Rich', 4.5, 'Igor Gavrik', 6, 25)
parrot_pet = Parrot('Rick', 5, 'Lera Simpson', 0.01, 20)
print(f'Dog name: {dog_pet.name}. Dog age: {dog_pet.age}. Dog master: {dog_pet.master}. Dog weight: {dog_pet.weight}. Dog height: {dog_pet.height}.')
print(f'Cat name: {cat_pet.name}. Cat age: {cat_pet.age}. Cat master: {cat_pet.master}. Cat weight: {cat_pet.weight}. Cat height: {cat_pet.height}.')
print(f'Parrot name: {parrot_pet.name}. Parrot age: {parrot_pet.age}. Parrot master: {parrot_pet.master}. Parrot weight: {parrot_pet.weight}. Parrot height: {parrot_pet.height}.')
dog_pet.change_weight(16)
# dog_pet.age = dog_pet.age + 1
# cat_pet.age = cat_pet.age + 1
# parrot_pet.age = parrot_pet.age + 1
# print(f'Dog age changed: {dog_pet.age}. Cat got older and now: {cat_pet.age}. Parrot followed them and went to: {parrot_pet.age}')
# print('')
# print(f'Dog {dog_pet.name} can {dog_pet.pet_jump}, {dog_pet.pet_run}, {dog_pet.pet_sleep} and like no others - {dog_pet.dog_bark()}.')
# print(f'Cat {cat_pet.name} can {cat_pet.pet_jump}, {cat_pet.pet_run}, {cat_pet.pet_sleep} and like no others - {cat_pet.cat_meow()}.')
# print(f'Parrot {parrot_pet.name} can {parrot_pet.pet_jump}, {parrot_pet.pet_run}, {parrot_pet.pet_sleep} and like no others - {parrot_pet.parrot_fly()}.')
