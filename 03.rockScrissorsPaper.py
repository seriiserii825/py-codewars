def rockScrissorsPaper(p1, p2):
    if p1 == p2:
        return 'Draw!'
    if (p1 == 'scrissors' and p2 == 'paper'):
        return 'Player 1 won!'
    if (p1 == 'scrissors' and p2 == 'rock'):
        return 'Player 2 won!'
    if (p1 == 'paper' and p2 == 'rock'):
        return 'Player 2 won!'
print(rockScrissorsPaper('rock', 'paper'))
