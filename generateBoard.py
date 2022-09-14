def determine_effects(intensity, randomseed, id, squares, move_chance=0.8):
    from random import seed, random
    seed(randomseed)
    if random() < intensity and id != 0:
        randomizer = (random()-0.5)*intensity
        if random() < move_chance:
            return {
                "move_steps": int(randomizer*40) if id+int(randomizer*40) in range(squares) else 0,
                "freeze_turns": 0
            }
        else:
            return {
                "move_steps": 0,
                "freeze_turns": int(randomizer*10)
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
        square.update(determine_effects(intensity, generationseed, id, count_squares, move_chance))
        squares.append(square)
    return(squares)

if __name__ == "__main__":
    from json import dump
    dump(generate_board(100, 0.75, 457478748373743), open("boards\\helloworld.json", "w"), indent=2)