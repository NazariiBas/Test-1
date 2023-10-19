# for number in range(1500, 2701):
#     if number % 7 == 0 and number % 5 == 0:
#         print(number)


# s1 = input("Дя переводу цельсія на фарангейти напишіть 1\nдля переводу фарангейтів в цельсії напишіть 2")
# s1 =int(s1)

# if s1 == 1:
#     choice = input("Введіть температуру в цельсіях:\n")
#     choice = int(choice)
#     print(choice * 9/5 +32)
# if s1 == 2:
#     choice = input("введіть температуру в фарангейтах:\n")
#     choice = int(choice)
#     print((choice - 32) * 5/9 )


# import random
# randomnumber = random.randint(1,99)



# count = 0
# while True:
#     guess = int(input("Введіть число від 1 до 99\n"))

#     if guess == randomnumber:
#         print("Добре вгадано") 
#         print("число: " + str(randomnumber))
#         print("Ви вгадали з:",count,"спроби")
#     elif guess != randomnumber:
#         print("ви не вгадали,спробуйте ще раз\n")
#         count += 1
#         if guess < randomnumber:
#             print("введіть більше число")
#         elif guess > randomnumber:
#             print("Введіть менше число")
          
    

# n = 5  

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
        