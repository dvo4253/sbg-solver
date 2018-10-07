from src.Move import Move, DIRECTION

def getMoves():
    move1 = Move(3,DIRECTION.RIGHT)
    move2 = Move(5,DIRECTION.UP)
    move3 = Move(2,DIRECTION.LEFT)

    return [move1, move2, move3]