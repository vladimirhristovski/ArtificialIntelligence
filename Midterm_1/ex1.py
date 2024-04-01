print("Hello world")

x = 34 - 23
y = "Hello"
z = 3.14
if z == 3.14 or y == "Hello":
    x += 1
    y += " World"
    print(x, y)
z = 5 / 2
print(z)
z = 5 // 2
print(z)  # celobrojno delenje
z = """"ab'c`de"""
print(z)
z = 10 ** 2  # stepen - power
print(z)
if "ll" in y:
    print(True)
if "lli" not in y:
    print(False)
x = 1
if 1 == x:
    print(True)
if 2 != x:
    print(False)
# immutable
m = x
x += 2
print(m)
print(x)
# torka - tuples
tu = (23, 'abc', 4.56, (2, "abs"), "def")
print(tu)
print(tu[1:-1])
print(tu[:-2])
print(tu[1:])
# string
st = "Hello"
print(st)
st = st.replace("Hello", "hello world")
sr = st
sr = sr.capitalize()
print(sr)
print(st)
st = """Multi
level
string"""
print(st)

# mutable
n = [1, 2, 3]
l = n
l.append(4)
print(n)
# list
li = ["Hello", "World", 5, 5.56]
lr = li
ly = li[:]  # deep copy
lr.append(10000)
print(li)
print(ly)
print(li[4], li[-5])
ln = [1, 3, 5, 6, 3, 2, 1]
print(ln)
tn = tuple(ln)
print(tn)

# dictionary
d = {1: "one", 2: "two", 3: ""}
print(d)
print(d[1])


# function
def my_fun(x, y):
    return x * y


print(my_fun(2, 5))


# lambda
def applier(param):
    applier(lambda x, y: x + y)
