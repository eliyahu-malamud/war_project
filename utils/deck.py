import random
def create_card(rank:str, suite:str) -> dict:
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'k', 'A']
    value = cards.index(rank) + 2
    return {'rank': rank, 'suite': suite, 'value': value}

def compare_cards(p1_card: dict, p2_card: dict) -> str:
    card1_value = p1_card['value']
    card2_value = p2_card['value']
    if card1_value > card2_value:
        return 'p1'
    elif card1_value < card2_value:
        return 'p2'
    else:
        return 'war'

def create_deck() -> list[dict]:
    my_list = []
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'k', 'A']
    suit = ['H', 'S', 'D', 'C']
    for x in suit:
        for y in rank:
            my_list.append(create_card(y, x))
    return my_list

def shuffle(deck: list[dict]) -> list[dict]:
    flag = 1000
    while flag:
        index1 = random.randint(0, 51)
        index2 = random.randint(0, 51)
        if index1 == index2:
            continue
        deck[index1], deck[index2] = deck[index2], deck[index1]
        flag -= 1
    return deck


