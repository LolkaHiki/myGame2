import random
import time

import Enemy
import Inventory
import main

def show_info(attacker, defender, attack_damage, defender_healing):
    """Выводит информацию о бое."""

    # Выводим информацию об атакующем

    print(f"{attacker.name} атакует {defender.name}.")
    print(f"Урон {attacker.name}: {attack_damage}")

    # Выводим информацию о защищающемся

    print(f"Здоровье {defender.name}: {defender_healing}")

    # Выводим результат атаки

    if defender_healing <= 0:
        print(f"{defender.name} побежден!")
    else:
        print(f"{defender.name} остался жив.")


while battle == 1:

    print("Выберите действие")
    print("1 - Атака        2 - Инвентарь        3 - Убежать")
    boi = int(input())

    if boi == 1:
        show_info(main.name, Enemy.enemy.name, main.attack_user, Enemy.enemy.health)
        if main.healing_user > 0 and Enemy.enemy.health > 0:
            Enemy.enemy.health = fight(main.attack_user, Enemy.enemy.health, main.name, Enemy.enemy.name)
            healing_user = fight(Enemy.enemy.attack, main.healing_user, Enemy.enemy.name, main.name)

        if main.healing_user <= 0 or Enemy.enemy.health <= 0:
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
    # Интересная механика. Игрок в любой момент может спасти свою жизнь или попробовать пойди по другому пути, мб полутать сундуки

