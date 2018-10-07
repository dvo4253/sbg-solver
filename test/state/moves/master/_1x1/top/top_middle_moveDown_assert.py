from src.Move import Move, DIRECTION

def getMoves():
    move1 = Move(2,DIRECTION.UP)
    move2 = Move(2,DIRECTION.DOWN)
    move3 = Move(5,DIRECTION.RIGHT)
    move4 = Move(6,DIRECTION.LEFT)

    return [move1, move2, move3, move4]