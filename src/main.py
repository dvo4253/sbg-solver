import stateUtils

state = stateUtils.readGameState('../state/SBP-bricks-level1.txt')
stateAdd = "Original State Address" + hex(id(state))
newState = stateUtils.cloneState(state)
newStateAdd = "New State Address " + hex(id(newState))
print("ORIGINAL")
print(stateAdd)
stateUtils.printState(state)
print("NEW")
print(newStateAdd)
stateUtils.printState(newState)

inGoal = "In Goal? " + str(stateUtils.inGoalCheck(state))
print(inGoal)