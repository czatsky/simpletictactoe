import string

dig = string.digits

game1 = '_________'
game = []
for i in game1:
    game.append(i)
space = [s for s in game if s == '_']
print(f'''---------
| {game[0]} {game[1]} {game[2]} |
| {game[3]} {game[4]} {game[5]} |
| {game[6]} {game[7]} {game[8]} |
---------''')
g = ['1 1','1 2','1 3','2 1','2 2','2 3','3 1','3 2','3 3']
x = 'X'
o = 'O'
varik = x

while True:
    X = [x for x in game if x == 'X']
    O = [y for y in game if y == 'O']
    space = [s for s in game if s == '_']
    if ((game[0] == game[1] and game[0] == game[2]) \
        or (game[0] == game[3] and game[3] == game[6]) \
        or (game[0] == game[4] and game[4] == game[8])) \
            and (len(X) - len(O) < 1 and len(O) - len(X) < 1) and (game[0] != '_'):
        print(f'{game[0]} wins1')
        break
    if ((game[3] == game[4] and game[4] == game[5]) \
          or (game[1] == game[4] and game[4] == game[7]) \
          or (game[2] == game[4] and game[4] == game[6])) \
            and (len(X) - len(O) <= 1 and len(O) - len(X) <= 1) and len(space) != 2 and (game[4] != '_'):
        print(f'{game[4]} wins2')
        break
    elif ((game[6] == game[7] and game[7] == game[8]) or (game[2] == game[5] and game[5] == game[8])) \
            and (len(X) - len(O) < 1 or len(O) - len(X) < 1) and (game[8] != '_'):
        print(f'{game[8]} wins3')
        break
    if not (((game[0] == game[1] and game[0] == game[2]) \
             or (game[0] == game[3] and game[3] == game[6]) \
             or (game[0] == game[4] and game[4] == game[8])) \
            or ((game[3] == game[4] and game[4] == game[5]) \
                or (game[1] == game[4] and game[4] == game[7]) \
                or (game[2] == game[4] and game[4] == game[6])) \
            or (game[6] == game[7] and game[7] == game[8]) \
            or (game[2] == game[5] and game[5] == game[8])) and len(space) == 0:
        print('Draw')
        break
    step = input()
    steps = step.split()
    if steps[0] not in dig or steps[1] not in dig:
        print('You should enter numbers!')
    elif (steps[0] != '1' and steps[0] != '2' and steps[0] != '3') or (steps[1] != '1' and steps[1] != '2' and steps[1] != '3'):
        print('Coordinates should be from 1 to 3!')
    else:
        a = g.index(step)
        if game[a] == 'X' or game[a] == 'O':
            print('This cell is occupied! Choose another one!')
        elif game[a] != 'X' and game[a] != 'O':
            game[a] = varik
            print(f'''---------
            | {game[0]} {game[1]} {game[2]} |
            | {game[3]} {game[4]} {game[5]} |
            | {game[6]} {game[7]} {game[8]} |
            ---------''')
            print(game)
            if game[a] == 'X':
                varik = o
            if game[a] == 'O':
                varik = x
