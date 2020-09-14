



# Complete the marsExploration function below.

def marsExploration(s):
    count = 0
    for i in range(len(s)):
        if ( i % 3 == 0 and s[i] != "S"):
            count+=1
        if( i % 3 == 1 and s[i] != "O"):
            count+=1
        if( i % 3 ==2 and  s[i] != "S"):
            count +=1
    return count    
