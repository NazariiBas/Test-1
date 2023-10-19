# 1-st task

import random

www = int(input("Введіть ваш номер в списку:"))
random_number = [random.randint(30,90)for _ in range(10 + www)]
print(random_number)

