import random
def generate_map(size):
  """
  Создает карту размером size x size.

  Args:
    size: Размер карты.

  Returns:
    Карта размером size x size.
  """

  map = [[0 for i in range(size)] for j in range(size)]

  # Заполняем матрицу числами 0(Пустая комнаята)

  for i in range(size):
    for j in range(size):
      map[i][j] = 0

  # Заполняем матрицу числами 2(Лут)
  count_two = int(size * size * 0.15)
  for i in range(count_two):
    i = random.randint(0, size - 1)
    j = random.randint(0, size - 1)
    map[i][j] = 2

  # Заполняем матрицу числами 1 (Враги)
  count_one = int(size * size * 0.2)
  for i in range(count_one):
      i = random.randint(0, size - 1)
      j = random.randint(0, size - 1)
      map [i][j] = 1

  # Заполняем матрицу числом 3 (Выход с уровня)
  i = random.randint(0, size - 1)
  j = random.randint(0, size - 1)
  map[i][j] = 3

  # Заполняем матрицу числом 4 (Фонтан со священной водой)
  i = random.randint(0, size - 1)
  j = random.randint(0, size - 1)
  map[i][j] = 4

  return map

  for i in range(size):
    for j in range(size):
      mapVision[i][j] = {"visible": False}

  return map, mapVision
map = generate_map(8)


for i in range(len(map)):
    print(map[i])

print('')

mapVision = [['#' for i in range(8)] for j in range(8)]

for i in range(len(mapVision)):
    for j in range(len(mapVision[i])):
        if map[i][j] == 1:
            print('M\t', end="")
        elif map [i][j] == 2:
            print ('C\t', end="")
        elif map [i][j] == 3:
            print ('E\t', end="")
        elif map [i][j] == 4:
            print ('F\t', end="")
        else:
            print('#\t', end="")
    print(' ')


def move_player(x, y):
    """
    Перемещает игрока на точку (x, y).

    Args:
      x: Координата x новой позиции игрока.
      y: Координата y новой позиции игрока.
    """

    global player_x, player_y

    player_x = x
    player_y = y

    # Проверяем, видима ли точка (x, y) для игрока.

    if not mapVision[x][y]["visible"]:
        # Если точка не видима, то делаем её видимой.
        mapVision[x][y]["visible"] = True

        # Обновляем состояние карты в этой точке.
        if map[x][y] == 1:
            mapVision[x][y] = "M"
        elif map[x][y] == 2:
            mapVision[x][y] = "C"
        elif map[x][y] == 3:
            mapVision[x][y] = "E"
        elif map[x][y] == 4:
            mapVision[x][y] = "F"
        elif map[x][y] == 0:
            mapVision[x][y] = '0'


def move():
    """
    Перемещает игрока в выбранном направлении.

    Args:
      direction: Направление движения игрока.
    """

    global player_x, player_y

    new_x = player_x
    new_y = player_y

    # Получаем ввод с клавиатуры.

    direction = input("Выберите направление движения (up, down, left, right): ")

    # Проверяем, что ввод корректный.

    if direction not in ["up", "down", "left", "right"]:
        return

    # Перемещаем игрока.

    if direction == "up":
        new_y -= 1
    elif direction == "down":
        new_y += 1
    elif direction == "left":
        new_x -= 1
    elif direction == "right":
        new_x += 1
