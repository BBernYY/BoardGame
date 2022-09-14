def create_characters(users):
    result = []
    for i in users:
        result.append({
            'name': i,
            'square': 0,
            'freeze': 0
        })
    return result
def main(board, characters, rollseed, rollsize=6): # Initial loop
    from random import random, seed
    characters = create_characters(characters)
    is_looping = True
    seed(rollseed)
    while is_looping:
        for i in characters:
            steps = 0
            if i['freeze'] > 0:
                i['freeze'] = i['freeze'] - 1
            else:
                roll = int((random()*rollsize-1) + 1) # random dice roll
                try:
                    steps = roll + board[i['square']+roll]['move_steps']
                except IndexError:
                    i['square'] = (len(board) - (len(board) + 1 - i['square']))
                if i['square'] == len(board) - 1:
                    is_looping = False
                    winner = i['name']
                else:
                    if steps != 0:
                        i['square'] = i['square'] + steps
                square = board[i['square']]
                if square['freeze_turns'] != 0:
                    i['freeze'] = square['freeze_turns']
    return winner
                



                


if __name__ == '__main__': # checks if the code is ran as a file
    import json
    from generateBoard import generate_board
    for i in range(100000):
        if i % 100 == 0:
            print(i)
        main(generate_board(100, 0.25, i), ['barry', 'harry'], i*2)
