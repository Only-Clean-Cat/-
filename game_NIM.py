from random import randint
import colorama
colorama.init()


MAX_BUNCHES = 5
MAX_BUNCHES_SIZE = 20
_holder = {}
_sorted_keys = None


#   Расположить кучки камней на столе
def put_stones():
    global _holder, _sorted_keys
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = randint(1, MAX_BUNCHES_SIZE)
    _sorted_keys = sorted(_holder.keys())


def take_from_bunch(position, quantity):
    if position in _holder:
        if _holder[position] < quantity or quantity < 1:
            cprint('Невозможный ход! Вы не можете взять больше чем есть!'
                   'Введите корректное количество "камней"', color='red')
            return False
        _holder[position] -= quantity
        return True
    else:
        return False

def get_bunches():
    res = []
    for key in _sorted_keys:
        res.append(_holder[key])
    return res

def is_gameover():
    return sum(_holder.values()) == 0
def replay():
    choise = input(colored('Хотите играть снова? Введите Y для продолжения'
                           ' или N для выхода', color='red')).upper()
    return choise == 'Y'

from termcolor import cprint, colored

cprint('Добро пожаловать в игру "НИМ"', color='green')
print('(версия: only-clean-cat 16.03.2024.1.0)')
cprint('Правила игры: На игровом столе лежат  "кучки" из камней,\n'
       ' игроки поочереди берут из них любое количество камней.\n'
       ' Проигрывает тот игрок, который, заберет последний\n камень. '
       'Номер "кучки" слева на право 1, 2, 3, 4, 5.', color='yellow')

while True:
    cprint('ПУСТЬ ПОБЕДИТ СИЛЬНЕЙШИЙ!', color='green')
    play_game = input(colored('Вы готовы играть? Введите Y (да) '
                              'или N (нет)', color='red')).upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
        break
    put_stones()
    user_number = 1
    while True:
        cprint('Текущая позиция', color='green')
        cprint(get_bunches(), color='green')
        user_color = 'blue' if user_number == 1 else 'yellow'
        cprint('Ход игрока {}'.format(user_number), color=user_color)
        where_from = input(colored('Откуда берем?', color=user_color))
        try:
            pos = int(where_from)
        except ValueError:
            cprint('Невозможный ход! Введите корректную цифру "кучки" от 1 до 5', color='red')
            continue
        if pos > 5 or pos < 1:
            cprint('Невозможный ход! Введите корректную цифру "кучки" от 1 до 5', color='red')
            continue
        how_many = input(colored('Сколько берем?', color=user_color))
        try:
            qua = int(how_many)
        except ValueError:
            cprint('Невозможный ход! Введите корректое число "камней"', color='red')
            continue
        step_successed = take_from_bunch(position=int(pos), quantity=int(qua))
        if step_successed:
            user_number = 2 if user_number == 1 else 1
        # else:
        #     return False
            # cprint('Невозможный ход! Введите корректную цифру', color='red')
        if is_gameover():
            # cprint('Выиграл игрок номер {}!'.format(user_number), color='red')
            break
    cprint('!!!!!!!!!!!!!!!!!!Выиграл ИГРОК {}!'.format(user_number), color='green')
    if not replay():
        break

