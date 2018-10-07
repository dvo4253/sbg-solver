from src.Move import Move, DIRECTION

def getMoves():
    move1 = Move(2,DIRECTION.LEFT)
    move2 = Move(2,DIRECTION.UP)
    move3 = Move(3,DIRECTION.RIGHT)
    move4 = Move(5,DIRECTION.UP)

    return [move1, move2, move3, move4]