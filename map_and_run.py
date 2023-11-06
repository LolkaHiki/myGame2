
def create_map():
    """Создаёт карту."""

    # Создаём список комнат

    rooms = []

    # Создаём комнату 1

    room_1 = {
        "name": "Комната 1",
        "description": "Вы находитесь в небольшой комнате с низким потолком. В центре комнаты стоит стол с двумя стульями.",
        "exits": {"север": "Комната 2", "юг": "Комната 3"},
    }
    rooms.append(room_1)

    # Создаём комнату 2

    room_2 = {
        "name": "Комната 2",
        "description": "Вы находитесь в большой комнате с высоким потолком. В центре комнаты стоит камин.",
        "exits": {"север": "Комната 1", "юг": "Комната 4"},
    }
    rooms.append(room_2)

    # Создаём комнату 3

    room_3 = {
        "name": "Комната 3",
        "description": "Вы находитесь в тёмной комнате. В комнате ничего нет.",
        "exits": {"север": "Комната 1", "юг": "Комната 5"},
    }
    rooms.append(room_3)

    # Создаём комнату 4

    room_4 = {
        "name": "Комната 4",
        "description": "Вы находитесь в комнате с выходом на улицу.",
        "exits": {"север": "Комната 2", "юг": "Улица"},
    }
    rooms.append(room_4)

    # Создаём комнату 5

    room_5 = {
        "name": "Комната 5",
        "description": "Вы находитесь в комнате с тупиком.",
        "exits": {"север": "Комната 3"},
    }
    rooms.append(room_5)

    # Возвращаем список комнат

    return rooms

matrix = [[ room_1,  25, 90, 74],
["Sachin", 410, 87.50, 130]
[56, "Abhinay", 253, 471]


def move(current_room, direction):
    """Перемещает игрока в другую комнату."""

    # Получаем список комнат

    rooms = create_map()

    # Проверяем, существует ли указанная комната

    if direction not in rooms[current_room]["exits"]:
        print("Вы не можете пойти в эту сторону.")
        return

    # Перемещаем игрока в другую комнату

    # global current_room
    # current_room = rooms[current_room]["exits"][direction]

    # Избавляемся от глобальной переменной current_room и передаем ее в функцию в качестве параметра

    current_room = rooms[current_room]["exits"][direction]

    # Выводим описание комнаты

    print(f"Вы находитесь в комнате {current_room['name']}.\n{current_room['description']}")


def main():
    """Основная функция."""

    # Создаём список комнат

    rooms = create_map()

    # Инициализируем текущую комнату

    current_room = rooms[0]

    # Запускаем цикл игры

    while True:

        # Выводим список доступных направлений

        print(f"Вы находитесь в комнате {current_room['name']}.")
        print("Вы можете пойти в следующие направления:")
        for direction in current_room["exits"]:
            print(direction)

        # Запрашиваем у игрока направление движения

        direction = input("В каком направлении вы хотите пойти? ")

        # Перемещаем игрока в другую комнату

        move(current_room, direction)


