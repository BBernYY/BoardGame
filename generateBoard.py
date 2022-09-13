from itertools import count


def determine_effects(intensity, randomseed, id, move_chance=0.8):
    from random import seed, random
    seed(randomseed)
    if random() < intensity:
        if random() < move_chance:
            value = int((random()-0.5)*int(intensity*random()*200))
            value = value if value != 0 else 1
            return {
                "move_steps": value if -value < id else id,
                "freeze_turns": 0
            }
        else:
            value = int((random())*(random()*intensity*10))
            value = value if value != 0 else 1
            return {
                "move_steps": 0,
                "freeze_turns": value if -value < id else id
            }
    else:
        return {
            "move_steps": 0,
            "freeze_turns": 0
        }


def generate_board(count_squares, intensity, randomseed, move_chance=0.8):
    squares = [{"id": 0, "move_steps": 0, "freeze_turns": 0}]
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
    dump(generate_board(100, 1.0, 100), open("boards\\helloworld.json", "w"), indent=2)