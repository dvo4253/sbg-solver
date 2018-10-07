from src.Move import Move, DIRECTION

def getMoves():
    move1 = Move(2,DIRECTION.UP)
    move2 = Move(2,DIRECTION.LEFT)
    move3 = Move(4,DIRECTION.UP)

    return [move1, move2, move3]