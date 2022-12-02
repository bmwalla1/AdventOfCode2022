

def run():
    inputfile = open('d2input.txt', 'r')
    Lines = inputfile.readlines()

    player_b_total = 0
    for line in Lines:
        split = line.replace('\n', '').split(' ')
        player_b_total += getRoundEndScore(getPlayerAMove(split[0]), getPlayerBMove(split[1]))

    # part 1
    print(player_b_total)

    player_b_total = 0
    for line in Lines:
        split = line.replace('\n', '').split(' ')
        player_b_total += getRoundEndScore(getPlayerAMove(split[0]), getPlayerBMovePart2(getPlayerAMove(split[0]), split[1]))

    # part 2
    print(player_b_total)


def getPlayerAMove(move):
    switch = {
        'A': 1,
        'B': 2,
        'C': 3,
    }
    return switch.get(move)


def getPlayerBMove(move):
    switch = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    return switch.get(move)


def getPlayerBMovePart2(player_a_move, outcome):
    # Lose
    if outcome == 'X':
        if player_a_move == 1:
            return 3
        elif player_a_move == 2:
            return 1
        elif player_a_move == 3:
            return 2
    # Draw
    elif outcome == 'Y':
        return player_a_move
    # Win
    elif outcome == 'Z':
        if player_a_move == 1:
            return 2
        if player_a_move == 2:
            return 3
        if player_a_move == 3:
            return 1


def getRoundEndScore(p_a_move, p_b_move):
    if p_b_move == 3 and p_a_move == 1:
        return p_b_move
    if p_b_move == 1 and p_a_move == 3:
        return p_b_move + 6
    if p_a_move < p_b_move:
        return p_b_move + 6
    if p_a_move > p_b_move:
        return p_b_move
    if p_a_move == p_b_move:
        return p_b_move + 3


if __name__ == '__main__':
    run()
