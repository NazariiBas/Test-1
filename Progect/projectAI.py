import random

def main():
    print("Ласкаво просимо до гри!")
    name = input("Введіть ваше ім'я: ").strip().title()
    print(f"Привіт, {name}!")
    
    print("Ви опинилися в загадковому лісі. Виберіть, куди ви хочете піти:")
    print("1. Піти глибше в ліс.")
    print("2. Повернути назад і вийти з лісу.")
    
    choice = input("Ваш вибір (1/2): ")
    
    if choice == '1':
        explore_forest()
    elif choice == '2':
        game_over("Ви вийшли з лісу, але зрозуміли, що загубились в невідомому місці.")
    else:
        game_over("Невірний вибір. Вас зачаровано, і ви прокляті літом у лісі.")

def explore_forest():
    print("Ви рушаєте глибше в ліс, і перед вами з'являється три стежки:")
    print("1. Праворуч веде до гори.")
    print("2. Прямо веде до стародавньої руїни.")
    print("3. Ліворуч веде до річки.")
    
    choice = input("Ваш вибір (1/2/3): ")
    
    if choice == '1':
        climb_mountain()
    elif choice == '2':
        explore_ruins()
    elif choice == '3':
        cross_river()
    else:
        game_over("Невірний вибір. Вас загубили в лісі.")

def climb_mountain():
    print("Ви піднімаєтесь на гору і знаходите скарби!")
    win("Вітаємо, ви виграли гру!")

def explore_ruins():
    print("Ви дістаєтеся до стародавньої руїни і знаходите дивну артефакт.")
    print("1. Взяти артефакт.")
    print("2. Покинути руїни.")
    
    choice = input("Ваш вибір (1/2): ")
    
    if choice == '1':
        game_over("Після взяття артефакту вас зачаровує і ви стаєте частиною руїн.")
    elif choice == '2':
        explore_forest()
    else:
        game_over("Невірний вибір. Вас зачаровує і ви стаєте частиною руїн.")

def cross_river():
    print("Ви дістаєтеся до річки і бачите місток через неї.")
    print("1. Перейти місток.")
    print("2. Повернути назад.")
    
    choice = input("Ваш вибір (1/2): ")
    
    if choice == '1':
        win("Ви успішно перейшли річку і знайшли вихід із лісу!")
    elif choice == '2':
        game_over("Ви повертаєтесь назад і загублюєтеся в лісі.")
    else:
        game_over("Невірний вибір. Вас зачаровує і ви стаєте частиною річки.")

def game_over(reason):
    print(f"Гра закінчилася: {reason}")
    play_again = input("Бажаєте спробувати знову? (так/ні): ")
    if play_again.lower() == 'так':
        main()
    else:
        print("Дякуємо за гру!")

def win(message):
    print(f"Ви виграли: {message}")
    play_again = input("Бажаєте спробувати знову? (так/ні): ")
    if play_again.lower() == 'так':
        main()
    else:
        print("Дякуємо за гру!")

if __name__ == "__main__":
    main()
