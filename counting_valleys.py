

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=0
    valley= 0
    for i in range(n):
        if s[i] == "U":
            level+=1
            if(level == 0):
                valley +=1
        else:
            level -=1
    return valley                
