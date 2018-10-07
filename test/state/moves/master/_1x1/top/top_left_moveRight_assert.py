from src.Move import Move, DIRECTION

def getMoves():
    move1 = Move(2,DIRECTION.UP)
    move2 = Move(2,DIRECTION.RIGHT)
    move3 = Move(3,DIRECTION.LEFT)
    move4 = Move(5,DIRECTION.UP)

    return [move1, move2, move3, move4]