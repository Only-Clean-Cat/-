test_board3 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#   Игровое поле
def display_board(test_board3):
    print(test_board3[7] + ' | ' + test_board3[8] + ' | ' + test_board3[9])
    print('--:---:---')
    print(test_board3[4] + ' | ' + test_board3[5] + ' | ' + test_board3[6])
    print('--:---:---')
    print(test_board3[1] + ' | ' + test_board3[2] + ' | ' + test_board3[3])
#   Выбор маркера Х или О
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Игрок 1 - выберите букву Х или O на ENG раскладке клавитатуры:').upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print('Игрок 1 выбрал: ', player1)
    print('Игрок 2 выбрал: ', player2)
    return (player1, player2)
#   Ход игрока
def place_marker(test_board3, marker, position):
    test_board3[position] = marker
#   Проверка на победу игрока
def win_check(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
     (board[4] == marker and board[5] == marker and board[6] == marker) or
     (board[7] == marker and board[8] == marker and board[9] == marker) or
     (board[1] == board[4] == board[7] == marker) or
     (board[2] == board[5] == board[8] == marker) or
     (board[3] == board[6] == board[9] == marker) or
     (board[1] == board[5] == board[9] == marker) or
     (board[3] == board[5] == board[7] == marker))


#   Кто будет ходить первым
import random
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Игрок 1'
    else:
        return 'Игрок 2'
#   Проверка пустых ячеек для хода
def space_check(test_board3, position):
    return test_board3[position] == ' '
#   Проверка на заполненность поля
def full_board_check(test_board3):
    for i in range(1, 10):
        if space_check(test_board3, i):
            return False
    return True
    print('Этот сектор уже занят')
#   Запрос к игроку на ход
def player_choice(test_board3):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(test_board3, position):
        position = int(input('Укажите номер сектора для хода от (1 - 9)'))
    return position
#   РЕВАНШ
def replay():
    choise = input('Хотите играть снова? Введите Y для продолжения или N для выхода').upper()
    return choise == 'Y'

#   СБОРКА ПРОЕКТА

print('Добро пожаловать в игру КРЕСТИКИ - НОЛИКИ!')
print('         (версия: only_clean_cat)')
test_board1 = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
test_board2 = ['#', 'X', 'Х', 'X', 'Х', 'X', ' ', 'X', ' ', 'X']

print('Игровое поле поделено на 9 секторов.\n'
      'Игрок вводит номер сектора куда собирается сделать ход.')
display_board(test_board1)
print('Побеждает игрок который разместит свой маркер Х или О.\n'
      'в трех соседних секторах по горизонтали или вертикали или диагонали.')
display_board(test_board2)
while True:
    play_game = input('Вы готовы играть? Введите Y (да) или N (нет)').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
        break
    test_board3 = [' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ']
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' ходит первым')
    while game_on:
        if turn == 'Игрок 1':
            #'Игрок 1'
            display_board(test_board3)
            position = player_choice(test_board3)
            place_marker(test_board3, player1_marker, position)
            if win_check(test_board3, player1_marker):
                display_board(test_board3)
                print('Игрок 1 ВЫИГРАЛ!')
                game_on = False
            else:
                if full_board_check(test_board3):
                    display_board(test_board3)
                    print('НИЧЬЯ! Вы достойные соперники!')
                    game_on = False
                else:
                    turn = 'Игрок 2'
        else:
            display_board(test_board3)
            position = player_choice(test_board3)
            place_marker(test_board3, player2_marker, position)
            if win_check(test_board3, player2_marker):
                display_board(test_board3)
                print('Игрок 2 ВЫИГРАЛ!')
                game_on = False
            else:
                if full_board_check(test_board3):
                    display_board(test_board3)
                    print('НИЧЬЯ! Вы достойные соперники!')
                    game_on = False
                else:
                    turn = 'Игрок 1'
    if not replay():
        break