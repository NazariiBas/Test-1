last_num = 1

array_length = 10 + last_num

my_array = []

for i in range(array_length):
    element = int(input(f"Введіть елемент {i + 1}: "))
    my_array.append(element)

max_element = max(my_array)

reversed_array = list(reversed(my_array))

print("Масив у зворотньому порядку:", reversed_array)
print("Максимальний елемент у масиві:", max_element)
