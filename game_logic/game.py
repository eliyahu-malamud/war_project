from utils import deck

def create_player(name: str = 'AI') -> dict:
    return {'name': name, 'hand': [], 'won_pile': []}

def init_game() -> dict:
    p1 = create_player('eliyahu')
    p2 = create_player()
    my_deck = deck.shuffle(deck.create_deck())
    p1['hand'] = my_deck[ : len(my_deck) // 2]
    p2['hand'] = my_deck[len(my_deck) // 2: ]
    return {'deck': my_deck, 'p1': p1, 'p2': p2}

def play_round(player_1: dict, player_2: dict)-> None:
    card1 = player_1['hand'].pop(0)
    card2 = player_2['hand'].pop(0)
    if deck.compare_cards(card1, card2) == 'p1':
        player_1['won_pile'].append(card1)
        player_1['won_pile'].append(card2)
        print(player_1['name'], 'is winning')
    elif deck.compare_cards(card1, card2) == 'p2':
        player_2['won_pile'].append(card1)
        player_2['won_pile'].append(card2)
        print(player_2['name'], 'is winning')
    else:
        print('draw')






