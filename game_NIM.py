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


from termcolor import cprint, colored

cprint('Добро пожаловать в игру "НИМ"', color='red')
cprint('Правила игры: На игровом столе лежит три кучки из камней,\n'
       ' игроки поочереди берут из них любое количество камней.\n'
       ' Выигрыват тот игрок, который, заберет последний\n камень. '
       'Номер "кучки" слева на право 1, 2, 3. ', color='yellow')
cprint('ПУСТЬ ПОБЕДИТ СИЛЬНЕЙШИЙ!', color='red')

put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', color='green')
    cprint(get_bunches(), color='green')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Ход игрока {}'.format(user_number), color=user_color)
    pos = input(colored('Откуда берем?', color=user_color))
    qua = input(colored('Сколько берем?', color=user_color))
    step_successed = take_from_bunch(position=int(pos), quantity=int(qua))
    if step_successed:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Невозможный ход!', color='red')
    if is_gameover():
        break

cprint('Выиграл игрок номер {}!'.format(user_number), color='red')

