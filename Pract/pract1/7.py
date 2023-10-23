last_num = 1

input_array = [i if i >= 0 else -i for i in range(10 + last_num)]

print("Заданий масив:", input_array)

for i in range(len(input_array)):
    if input_array[i] < 0:
        input_array[i] = -input_array[i]

print("Масив з негативних на позитивні:", input_array)
