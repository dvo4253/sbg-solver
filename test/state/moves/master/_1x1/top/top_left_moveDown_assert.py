from src.Move import Move, DIRECTION

def getMoves():
    move1 = Move(2,DIRECTION.DOWN)
    move2 = Move(5,DIRECTION.LEFT)

    return [move1, move2]