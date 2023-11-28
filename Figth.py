import Inventory
import random
import Enemy
import time
import User

battle = 1



while battle == 1:

    print("Выберите действие")
    print("1 - Атака        2 - Инвентарь        3 - Убежать")
    boi = int(input())

    if boi == 1:
        def dice(sides=6):
            return random.randint(1, sides)


        def fight(attack_damage, defender_healing, attack_name, defender_name):
            cube = dice(10)
            if cube == 1:
                print(f"{attack_name} промахнулся")
                time.sleep(2)
            elif cube == 10:
                defender_healing -= attack_damage * 2
                print(f"{defender_name} осталось {defender_healing} здоровья *критический урон*")
                time.sleep(2)
            else:
                defender_healing -= attack_damage
                print(f"{defender_name} осталось {defender_healing} здоровья")
                time.sleep(2)
            return defender_healing



        if healing_user > 0 and enemy.health > 0:
            enemy.health = fight(attack_user, enemy.health, name, enemy.name)
            healing_user = fight(enemy.attack, healing_user, enemy.name, name)

        if healing_user <= 0 or enemy.health <= 0:
            battle = 0
    # Расчет урона методом кубика + задержка времени при подсчёте урона
    # Добавить в боёвку вариативность, как в с Дворфом. Например, босса Дракона можно будет задобрить с помощью какой-нибудь хренью, которая занимает большую часть инвенторя.
    elif boi == 2:
        print(Inventory.inventory.show_inventory())
        choice = input()
        if choice == beer and enemy == Enemy.Dvorf:
            enemy.is_drunk = True
            print(f"Дворф выпил пиво и стал добрым")
            print(f"Дворф: 'Ну ладно, давай договоримся. Я не буду тебя трогать, если ты мне дашь ещё пива.'")
            choice = input()
            if choice == beer:
                print(f"Дворф: 'Спасибо, приятель. Я тебе ещё отплачу.'")
                enemy.health = 100
                battle = 0
            else:
                print(f"Дворф: 'Ну ладно, тогда я тебя убью.'")
    # Пиво не работает

    # Тут взаимодействие с инвентарём во время боя

    else:
        print(f"Вы сбежали с поля боя, но вы сохранили свою жизнь. Ваше здоровье {healing_user}")
        battle = 0


# print(f"Вы встретили монстра - {enemy.name}")
# print("БОЙ")
# time.sleep(2)
# battle = 1
#
#
# while battle == 1:
#
#     print("Выберите действие")
#     print("1 - Атака        2 - Инвентарь        3 - Убежать")
#     boi = int(input())
#
#     if boi == 1:
#         def dice(sides=6):
#             return random.randint(1, sides)
#
#
#         def fight(attack_damage, defender_healing, attack_name, defender_name):
#             cube = dice(10)
#             if cube == 1:
#                 print(f"{attack_name} промахнулся")
#                 time.sleep(2)
#             elif cube == 10:
#                 defender_healing -= attack_damage * 2
#                 print(f"{defender_name} осталось {defender_healing} здоровья *критический урон*")
#                 time.sleep(2)
#             else:
#                 defender_healing -= attack_damage
#                 print(f"{defender_name} осталось {defender_healing} здоровья")
#                 time.sleep(2)
#             return defender_healing
#
#
#
#         if healing_user > 0 and enemy.health > 0:
#             enemy.health = fight(attack_user, enemy.health, name, enemy.name)
#             healing_user = fight(enemy.attack, healing_user, enemy.name, name)
#
#         if healing_user <= 0 or enemy.health <= 0:
#             battle = 0
#     # Расчет урона методом кубика + задержка времени при подсчёте урона
#     # Добавить в боёвку вариативность, как в с Дворфом. Например, босса Дракона можно будет задобрить с помощью какой-нибудь хренью, которая занимает большую часть инвенторя.
#     elif boi == 2:
#         print(Inventory.inventory.show_inventory())
#         choice = input()
#         if choice == beer and enemy == Enemy.Dvorf:
#             enemy.is_drunk = True
#             print(f"Дворф выпил пиво и стал добрым")
#             print(f"Дворф: 'Ну ладно, давай договоримся. Я не буду тебя трогать, если ты мне дашь ещё пива.'")
#             choice = input()
#             if choice == beer:
#                 print(f"Дворф: 'Спасибо, приятель. Я тебе ещё отплачу.'")
#                 enemy.health = 100
#                 battle = 0
#             else:
#                 print(f"Дворф: 'Ну ладно, тогда я тебя убью.'")
#     # Пиво не работает
#
#     # Тут взаимодействие с инвентарём во время боя
#
#     else:
#         print(f"Вы сбежали с поля боя, но вы сохранили свою жизнь. Ваше здоровье {healing_user}")
#         battle = 0