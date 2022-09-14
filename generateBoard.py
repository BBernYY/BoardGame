def determine_effects(intensity, randomseed, id, squares, move_chance=0.8):
    from random import seed, random
    seed(randomseed)
    if random() < intensity and id != 0:
        if random() < move_chance:
            value = int((random()-0.5)*int(intensity*random()*200))
            value = value if value != 0 else 1
            value = value if -value < id else id
            return {
                "move_steps": value if value < squares - id else id - 1,
                "freeze_turns": 0
            }
        else:
            value = int((random())*(random()*intensity*10))
            return {
                "move_steps": 0,
                "freeze_turns": value if value != 0 else 1
            }
    else:
        return {
            "move_steps": 0,
            "freeze_turns": 0
        }


def generate_board(count_squares, intensity, randomseed, move_chance=0.8):
    squares = []
    from random import seed, random
    generationseed = seed(randomseed)
    for id in range(count_squares):
        random()
        square = {"id": id}
        square.update(determine_effects(intensity, generationseed, id, move_chance))
        squares.append(square)
    return(squares)

if __name__ == "__main__":
    from json import dump
    dump(generate_board(100, 1.0, 8938728339), open("boards\\helloworld.json", "w"), indent=2)