import math

def calculate_func(a, x):
    b = math.sin(x) ** 3 - a
    z = abs(1 - math.sqrt(a) - math.cos(b))
    return b, z

with open("input.txt", "r") as input_file:
    lines = input_file.read().split(' ')

mylist = list(map(float,lines))
# a, x = map(float, lines)
a, x = mylist[0],mylist[1]
b, z = calculate_func(a, x)

print("a =", a)
print("x =", x)
print("b =", b)
print("z =", z)

with open("output.txt", "w") as output_file:
    output_file.write(f"a = {a}\n")
    output_file.write(f"x = {x}\n")
    output_file.write(f"b = {b}\n")
    output_file.write(f"z = {z}\n")

