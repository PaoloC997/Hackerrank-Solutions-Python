

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount=0
    bcount=0
    for i in range(len(apples)):
        temp=a+apples[i]
        if temp in range(s,t+1):
            acount+=1
    for i in range(len(oranges)):
        temp=b+oranges[i]
        if temp in range(s,t+1):
            bcount+=1 
    print(acount)
    print(bcount)     