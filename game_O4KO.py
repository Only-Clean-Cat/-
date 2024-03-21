import random
import colorama
colorama.init()
from termcolor import cprint, colored

#   Переменные для хранения масти, достонства и значения карт.
suits = ('Червы', 'Бубны', 'Пики', 'Трефы')
ranks = ('Двойка', 'Тройка', 'Четверка', 'Пятерка', 'Шестерка', 'Семерка',
         'Восьмерка', 'Девятка', 'Десятка', 'Валет', 'Дама', 'Король', 'Туз') * 4
values = {'Двойка': 2, 'Тройка': 3, 'Четверка': 4, 'Пятерка': 5, 'Шестерка': 6, 'Семерка': 7,
          'Восьмерка': 8, 'Девятка': 9, 'Десятка': 10, 'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}

playing = True


#   Создание класса для хранения отдельной карты и вывода информации о карте

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' ' + self.suit


#   Создание колоды карт для игры

class Deck:
    def __init__(self):  # создание колод
        self.deck = []  # начинаем с пустого списка
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    # def __str__(self):      # для отладки во время разработки
    #     deck_comp = ''
    #     for card in self.deck:
    #         deck_comp += '\n' + card.__str__()
    #     return 'В колоде осталось: ' + deck_comp

    def shuffle(self):  # для перемешивания колод
        random.shuffle(self.deck)

    def deal(self):  # сдача карты
        single_card = self.deck.pop()
        return single_card


#   ТЕСТИРУЕМ
# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)

#   Карты на руках у игрока

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # атрибут для тузов

    def add_card(self, card):
        self.cards.append(card)  # card из объекта Deck
        self.value += values[card.rank]
        if card.rank == 'Туз':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10  # сбрасываем туз до 1 при переборе
            self.aces -= 1


#   ТЕСТИРУЕМ
# test_deck = Deck()
# test_deck.shuffle()
# test_player = Hand()     # игрок
# pulled_card = test_deck.deal()   #  получаем карту
# print(pulled_card)
# test_player.add_card(pulled_card)
# print(test_player.value)

#   Игровые фишки на руках игрока

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


#   Ставка игрока на кон

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(colored('Сколько Вы ставите? ', color='magenta')))
        except:
            cprint('Пожалуйста, введите корректное число фишек. '
                   'Доступно: {}'.format(chips.total), color='red')
        else:
            if chips.bet > chips.total:
                cprint('У Вас недостаточно фишек для такой ставки. '
                       'Доступно: {}'.format(chips.total), color='red')
            else:
                break


#   Игрок берет дополнительные карты

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


#   Берем еще или стоп

def hit_or_stand(deck, hand):
    global playing  # для контроля цикла
    while True:
        x = input(colored('Еще карту или достаточно? Введите h (еще) '
                          'или s (хватит)', color='magenta')).lower()
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            cprint('Теперь ход "ДИЛЕРА".', color='magenta')
            playing = False
        else:
            cprint('Ваш ответ не понятен. Введите "h" или "s" на '
                   'ENG раскладке клавиатуры', color='red')
            continue
        break

#   Отображение игрового стола

def show_some(player, dealer):
    cprint('\nКарты "ДИЛЕРА":', color='blue')
    print(' <карта скрыта>')
    print('', dealer.cards[1])
    cprint('\nВаши карты:', color='yellow')
    print(*player.cards, sep='\n')
    print('Ваши карты, очков: ', player.value)


def show_all(player, dealer):
    cprint('\nКарты "ДИЛЕРА":', color='blue')
    print(*dealer.cards, sep='\n')
    print('Карты "ДИЛЕРА", очков ', dealer.value)
    cprint('\nВаши карты:', color='yellow')
    print(*player.cards, sep='\n')
    print('Ваши карты, очков: ', player.value)

#   Завершение игры

def player_busts(player, dealer, chips):
    cprint('Превышена сумма карт 21..... увы! Вы проиграли!', color='red')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    cprint('Вы выиграли!', color='yellow')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    cprint('"ДИЛЕР" проирал! Превышена сумма карт 21', color='yellow')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    cprint('"ДИЛЕР" выиграл. Вам мимо кассы!', color='red')
    chips.lose_bet()


def push(player, dealer, chips):
    cprint('Ничья! Ставки возвращаются игрокам.', color='yellow')

#   СБОРКА ПРОЕКТА

cprint('Добро пожаловать в игру "БЛЭКДЖЕК"!', color='green')
print('версия: Only-Clean-Cat 21.03.2024.1.0')

    #   Фишки игрока

player_chips = Chips()
while True:

        #   Создаем и перемешиваем колоду. Раздаем карты

        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        #   Показываем карты

        show_some(player_hand, dealer_hand)

        #   Ставка игрока
        cprint('\n Ваш счет равен: {}'.format(player_chips.total), color='green')
        take_bet(player_chips)

        while playing:
            # берем еще?
            hit_or_stand(deck, player_hand)
            # показываем карты
            show_some(player_hand, dealer_hand)
            # считаем результат раздачи
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            #  Показываем все карты
            show_all(player_hand, dealer_hand)
            #  Подсчет результатов на столе
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand, player_chips)
        cprint('\n Ваш счет равен: {}'.format(player_chips.total), color='green')
        if player_chips.total == 0:
            cprint('У Вас недостаточно фишек для продолжения игры. '
                   'Пожалуста, пополните счет или приходите завтра.)))', color='red')
            playing = False
            break
        new_game = input(colored('Хотите сыграть снова? Введите Y (да) или '
                         'N (нет) на ENG раскладке клавиатуры.', color='magenta').upper())
        if new_game[0] == 'Y':
            playing = True
            continue
        else:
            cprint('Спасибо за игру! Будем рады видеть Вас снова!', color='green')
            break



