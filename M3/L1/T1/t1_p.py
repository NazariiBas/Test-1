def dialog(question, right_answer, comment1, comment2):
    s = input(question)
    if s == right_answer:
        print(comment1)
    else:
        print(comment2)


dialog("Яку мову програмування ми вивчаємо?", "Python",
       "Правильно!", "Правильна ідповідь Python")
