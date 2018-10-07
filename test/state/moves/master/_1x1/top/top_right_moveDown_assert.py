from src.Move import Move, DIRECTION

def getMoves():
    move1 = Move(2,DIRECTION.DOWN)
    move2 = Move(2,DIRECTION.UP)
    move3 = Move(6,DIRECTION.RIGHT)

    return [move1, move2, move3]