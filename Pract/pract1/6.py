
last_num = 5

M = 1

X = [i for i in range(1, 11 + last_num)]
Y = [x for x in X if abs(x) > M]

print("Число M:", M)
print("Масив X:", X)
print("Масив Y (елементи більше за модулем", M, "):", Y)
