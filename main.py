from game_logic import game
if __name__ == '__main__':
    game_dict = game.init_game()
    while game_dict['p1']['hand'] and game_dict['p2']['hand']:
        game.play_round(game_dict['p1'], game_dict['p2'])
    if len(game_dict['p1']['won_pile']) > len(game_dict['p2']['won_pile']):
        print(f'{game_dict['p1']['name']} wind the game!')
    elif len(game_dict['p1']['won_pile']) < len(game_dict['p2']['won_pile']):
        print(f'{game_dict['p2']['name']} wind the game!')
    else:
        print('the game ends as draw!')

