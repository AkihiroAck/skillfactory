game_progress = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

print(' ', 0, 1, 2, '\n0', *game_progress[0], '\n1', *game_progress[1], '\n2', *game_progress[2], '\n')

player = 'X'


def is_over():
    if any(all(cell == player for cell in row) for row in game_progress) or any(all(game_progress[row][col] == player for row in range(3)) for col in range(3)) or all([game_progress[i][i] == player for i in range(3)]) or all([game_progress[i][2-i] == player for i in range(3)]):
        print(f'Player: - {player} - Win!')
        return True
    elif '-' not in [x for i in game_progress for x in i]:
        print('No Winner!')
        return True
    else:
        return False
        

def player_move():
    while True:
        try:
            p_move = input('Input: ')
            if len(p_move) == 2 and p_move[0] in '012' and p_move[1] in '012' and game_progress[int(p_move[0])][int(p_move[1])] == '-':
                game_progress[int(p_move[0])][int(p_move[1])] = player
                break
            else:
                print('Incorrect empty!')
        except ValueError:
            print('Error!')
            
            
def game():
    global player
    while True:
        print('Player:', player)
        player_move()
        print(' ', 0, 1, 2, '\n0', *game_progress[0], '\n1', *game_progress[1], '\n2', *game_progress[2], '\n')
        if is_over():
            break
        player = 'X' if player == 'O' else 'O'


game()
