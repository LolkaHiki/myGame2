import pygame
import User_hero
# Определяем класс персонажа
class Character:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def gain_experience(self, experience):
        self.experience += experience

        if self.experience >= self.level_up_experience:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += self.level * 10
        self.attack += self.level * 2
        self.defense += self.level * 1

# Создаем персонажа
character = User_hero.Character

# Основной игровой цикл
while True:
    # Обновляем состояние игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Рисуем игру
    pygame.display.update()

    # Даем персонажу получить опыт
    character.gain_experience(10)

    # Проверяем, не достиг ли персонаж следующего уровня
    if character.level_up_experience < character.experience:
        # Даем персонажу повысить уровень
        character.level_up()

        # Выводим сообщение об этом
        print(f"Персонаж {character.name} достиг уровня {character.level}")

    # Вводим имя игрока
    name = input("Введите имя игрока: ")

    # Обновляем имя персонажа
    character.name = name
