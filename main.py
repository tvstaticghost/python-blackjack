import random

player_hand = []
computer_hand = []

computer_score = 0

cards = [11, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10, 10, 10, 10]

def get_random_index():
    random_num = random.randint(0, len(cards) - 1)
    return random_num

def get_initial_cards():
    for i in range(0, 2):
        player_hand.append(cards[get_random_index()])
        computer_hand.append(cards[get_random_index()])

def get_card():
    player_hand.append(cards[get_random_index()])

def calculate_hand_total(hand):
    score = 0
    has_ace = False
    if hand == 'player':
        for i in range(0, len(player_hand)):
            if player_hand[i] == 11:
                has_ace = True
            score += player_hand[i]
        if score > 21 and has_ace == True:
            score -= 10
        return score
    elif hand == 'computer':
        for i in range(0, len(computer_hand)):
            if computer_hand[i] == 11:
                has_ace = True
            score += computer_hand[i]
        if score > 21 and has_ace == True:
            score -= 10
        return score
    
def call_winner():
    if calculate_hand_total('player') < calculate_hand_total('computer'):
        print(f'\tYour final hand: {player_hand}, final score: {calculate_hand_total("player")}')
        print(f'\tComputer\'s final hand: {computer_hand}, final score: {calculate_hand_total("computer")}')
        print(f'You lose :(')
    elif calculate_hand_total('player') > calculate_hand_total('computer'):
        print(f'\tYour final hand: {player_hand}, final score: {calculate_hand_total("player")}')
        print(f'\tComputer\'s final hand: {computer_hand}, final score: {calculate_hand_total("computer")}')
        print(f'You win!! :)')
    else:
        print(f'\tYour final hand: {player_hand}, final score: {calculate_hand_total("player")}')
        print(f'\tComputer\'s final hand: {computer_hand}, final score: {calculate_hand_total("computer")}')
        print(f'It\'s a draw!')
    
def reset():
    player_hand.clear()
    computer_hand.clear()

def play_round():
    bust = False
    get_initial_cards()

    print(f'\tYour cards: {player_hand}, current score: {calculate_hand_total("player")}')
    print(f'\tComputer\'s first card: {computer_hand[0]}')
    hit = input(f'Type "y" to get another card, type "n" to pass: ')
    while hit.lower() == 'y':
        get_card()
        if calculate_hand_total('player') > 21:
            print(f'\tYour final hand: {player_hand}, final score: {calculate_hand_total("player")}')
            print(f'\tComputer\'s final hand: {computer_hand}, final score: {calculate_hand_total("computer")}')
            print(f'You lose :(')
            bust = True
            break
        else:
            print(f'\tYour cards: {player_hand}, current score: {calculate_hand_total("player")}')
            print(f'\tComputer\'s first card: {computer_hand[0]}')
            hit = input(f'Type "y" to get another card, type "n" to pass: ')

    if bust == True:
        play_again = input('Do you want to play a game of Blackjack? Type "y" or "n": ')
        if play_again.lower() == 'y':
            reset()
            play_round()
        else:
            exit
    else:
        call_winner()
        play_again = input('Do you want to play a game of Blackjack? Type "y" or "n": ')
        if play_again.lower() == 'y':
            reset()
            play_round()
        else:
            exit

play_game = input('Do you want to play a game of Blackjack? Type "y" or "n": ')

if play_game.lower() == 'y':
    play_round()
else:
    exit