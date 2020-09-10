


# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    absCatA, absCatB = abs(x - z), abs(y - z)
    if absCatA == absCatB:
        return "Mouse C"
    else :
        return "Cat A" if absCatB > absCatA else "Cat B"         
