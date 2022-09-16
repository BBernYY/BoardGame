def create_characters(users):
    result = []
    for i in users:
        result.append({
            'name': i,
            'square': 0,
            'freeze': 0
        })
    return result
def choose_dice(dice):
    from random import choice
    return choice(dice)
def main(board, characters, rollseed, dice): # Initial loop
    from random import seed, choice
    characters = create_characters(characters)
    is_looping = True
    seed(rollseed)
    while is_looping:
        for i in characters:
            steps = 0
            if i['freeze'] > 0:
                i['freeze'] = i['freeze'] - 1
            else:
                roll = choice(choose_dice(dice)) # random dice roll
                if i['square'] == len(board) - 1:
                    is_looping = False
                    winner = i['name']
                try:
                    steps = roll + board[i['square']+roll]['move_steps']
                except IndexError:
                    i['square'] = (len(board) - (len(board) + 1 - i['square']))
                else:
                    if steps != 0:
                        i['square'] = i['square'] + steps
                square = board[i['square']]
                if square['freeze_turns'] != 0:
                    i['freeze'] = square['freeze_turns']
    return winner
                



                


if __name__ == '__main__': # checks if the code is ran as a file
    from generateBoard import generate_board
    print(main(generate_board(20, 0.25, 69), ['a', 'b'], 21, [[1, 1, 4, 4, 8, 8], [1, 1, 2, 2, 3, 3], [3, 3, 5, 5, 9, 9]]))
