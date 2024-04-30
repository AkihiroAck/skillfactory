import random


# ===========================================================================================================================================================


class Ship:
    def __init__(self, points):
        self.points = points


class Board:
    def __init__(self, ships):
        self.ships = ships
        self.grid = [['О' for _ in range(6)] for _ in range(6)]
        self.place_ships()
    
    def display(self, hide: bool = False):
        if hide:
            print(f'  |', end='')
            for i in range(6):
                print(f' {i + 1} |', end='')
            print()
        
            for r in range(6):
                row = []
                for c in range(6):
                    if self.grid[r][c] == '■':
                        row.append('О')  # Скрываем корабли
                    else:
                        row.append(self.grid[r][c])
                print(f"{r + 1} | {' | '.join(row)} |")
        else:
            print(f'  |', end='')
            for i in range(6):
                print(f' {i + 1} |', end='')
            print()
        
            for i in range(6):
                print(f'{i + 1} |', end='')
                for x in range(6):
                    print(f' {self.grid[i][x]} |', end='')
                print()
    
    def place_ships(self):
        for ship in self.ships:
            for point in ship.points:
                row, col = point
                self.grid[row][col] = '■'


# ===========================================================================================================================================================


def generate_ships():
    ships = []
    # Генерация кораблей
    # Добавьте свой код для генерации кораблей в соответствии с требованиями

    board = [['О' for _ in range(6)] for _ in range(6)]

    # Создаем 1 корабль на 3 клетки
    ship_create(board, 3, ships)

    # Создаем 2 корабля на 2 клетки
    for _ in range(2):
        ship_create(board, 2, ships)
    
    return ships


# -----------------------------------------------------------------------------------------------------------------------------------------------------------


def ship_create(board, ship_length, ships):
    while True:
        # Случайно выбираем направление корабля (горизонтальное или вертикальное)
        is_horizontal = random.choice([True, False])
        
        # Генерируем случайные координаты начальной точки корабля
        if is_horizontal:
            start_row = random.randint(0, len(board[0]) - 1)
            start_col = random.randint(0, len(board) - ship_length)
        else:
            start_row = random.randint(0, len(board[0]) - ship_length)
            start_col = random.randint(0, len(board) - 1)
        
        # Проверяем, что все ячейки, которые должны занять корабль, пусты
        for i in range(ship_length):
            if is_horizontal:
                if board[start_row][start_col + i] != 'О':
                    break
            else:
                if board[start_row + i][start_col] != 'О':
                    break
        else:
            # Размещаем корабль на поле
            points = []
            for i in range(ship_length):
                if is_horizontal:
                    board[start_row][start_col + i] = '■'
                    points.append((start_row, start_col + i))
                else:
                    board[start_row + i][start_col] = '■'
                    points.append((start_row + i, start_col))
            ships.append(Ship(points))
            break


# -----------------------------------------------------------------------------------------------------------------------------------------------------------


def player_turn(enemy_board, player):
    if player == 1:
        while True:
            try:
                row = int(input('Введите номер строки: ')) - 1
                if row < 0 or 5 < row:
                    raise ValueError('Неверная строка')
                
                col = int(input('Введите номер столбца: ')) - 1
                if col < 0 or 5 < col:
                    raise ValueError('Неверный столбец')
                
                if enemy_board.grid[row][col] == 'О':  # Если попали в пустую клетку
                    enemy_board.grid[row][col] = 'T'  # Обозначаем попадание
                
                elif enemy_board.grid[row][col] == '■':  # Если попали в корабль
                    enemy_board.grid[row][col] = 'Х'  # Обозначаем попадание в корабль
                
                else:
                    raise ValueError('Вы уже стреляли в эту клетку')
                
            except Exception as e:
                print(e)
            else:
                break
    else:
        while True:
            try:
                row = random.randint(0, 5)
                col = random.randint(0, 5)
                print(f'Cтрока: {row+1}\nCтолбец: {col+1}')
                if enemy_board.grid[row][col] == 'О':  # Если попали в пустую клетку
                    enemy_board.grid[row][col] = 'T'  # Обозначаем попадание
                elif enemy_board.grid[row][col] == '■':  # Если попали в корабль
                    enemy_board.grid[row][col] = 'Х'  # Обозначаем попадание в корабль
                else:
                    raise ValueError('Вы уже стреляли в эту клетку')
            except Exception as e:
                print(e)
            else:
                break


def check_win(board):
    for row in board.grid:
        for cell in row:
            if cell == '■':
                return False
    return True


def play_game():
    player_board = Board(generate_ships())
    computer_board = Board(generate_ships())

    # Чит - скрыть или показать корабли врага (True|False)
    hide = True
    print()
    print('computer_board')
    computer_board.display(hide)
    print()
    print('player_board')
    player_board.display()
    
    player = 1
    while True:
        print()
        print(f'Игрок: {player}')
        if player == 1:
            player_turn(computer_board, player)
            print()
            print('computer_board')
            computer_board.display(hide)
            if check_win(computer_board):
                print(f'\nИгрок: {player} ПОБЕДИЛ')
                break
                
        else:
            player_turn(player_board, player)
            print()
            print('player_board')
            player_board.display()
            if check_win(player_board):
                print(f'\nИгрок: {player} ПОБЕДИЛ')
                break
            
        player = 2 if player == 1 else 1
    input()


if __name__ == "__main__":
    play_game()
