x = 100
if x:
    print(True)
else:
    print(False)
y = 0
if y:
    print(False)
else:
    print(True)
x = 2
if x == 3:
    print("3")
elif x == 2:
    print("2")
else:
    print("Other")
fruit = "apple"
is_apple = True if fruit == "apple" else False
print(is_apple)
x = 3
while x < 5:
    print(x)
    x += 1
else:
    print("out")
text = "hello world"
for e in text:
    print(e)

coll = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]
for (x, y) in coll:
    print(x)

l = range(2, 6)
for e in l:
    print(e)

fruits = ["banana", "apple", "mango"]
for fruit in fruits:
    print(fruit)

for index in range(len(fruits)):
    print(fruits[index])

ages = {'sam': 4, "mary": 3, 'bill': 2}
for age in ages.keys():
    print(age, ages[age])

x = 1
assert (x == 1)
'''frla isklucok ako true'''

lista = [1, 2, 3, 4, 5, 6]
lista = [elem * 2 for elem in lista]
print(lista)

coll = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]
coll = [n * 3 for (x, n) in coll]
print(coll)


def subtract(a, b):
    return a - b


lista2 = [(1, 2), (3, 4), (5, 6)]
lista2 = [subtract(y, x) for (x, y) in lista2]
print(lista2)

lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista3 = [e * 2 for e in lista3 if e % 2 == 0]
print(lista3)
'''filter i *2'''

lista4 = [1, 2, 3, 4, 5]
lista4 = [e * 2 for e in [i + 1 for i in lista4]]
print(lista4)

lista5 = [[3, 'a', 9], [2, 7], [4, 1, 8, 'd']]
flatten = [val for elem in lista5 for val in elem]
print(flatten)

money = 2000


def add_money():
    global money
    money = money + 1000


print(money)
add_money()
print(money)


class Student:
    x = 23

    def __init__(self, name, age):
        self.full_name = name
        self.age = age

    def get_age(self):
        return self.age

    def increment(self):
        self.__class__.x += 1


b = Student("Vladimir", 20)
print(b.get_age())
print(b.full_name)

name = getattr(b, "full_name")
print(name)

age = getattr(b, "get_age")()
print(age)

print(hasattr(b, "get_age"))
print(hasattr(b, "full_name"))

b.increment()
print(b.__class__.x)


class AISrudent(Student):
    __privatna_promelnliva = 0

    def __init__(self, name, age, section):
        super(AISrudent, self).__init__(name, age)
        self.section_num = section

    def get_age(self):
        print("Age : " + str(self.age))
