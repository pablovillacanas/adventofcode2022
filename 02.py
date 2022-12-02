game_dict = {
    'X': {  # ROCK
        'val': 1,
        'A': 3,  # ROCK
        'B': 0,  # SCISSORS
        'C': 6,  # PAPER
    },
    'Y':  # PAPER
    {
        'val': 2,
        'A': 6,  # ROCK
        'B': 3,  # PAPER
        'C': 0,  # SCISSORS
    },
    'Z': {  # SCISSORS
        'val': 3,
        'A': 0,  # ROCK
        'B': 6,  # PAPER
        'C': 3,  # SCISSORS
    },
}
with open('input02.txt', 'r') as f:
    plays = f.read().split('\n')
    play_sum = 0
    play_sum_tricked = 0
    for play in plays:
        opponent = play.split(' ')[0]
        me = play.split(' ')[1]
        play_result = game_dict[me]['val'] + game_dict[me][opponent]
        play_sum += play_result
        # find key that has desired outcome regarding opponent choose
        desired_value = 0 if me == 'X' else 3 if me == 'Y' else 6
        for i in game_dict:
            if game_dict[i][opponent] == desired_value:
                play_sum_tricked += game_dict[i]['val'] + desired_value
    print(play_sum)
    print(play_sum_tricked)
