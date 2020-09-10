

# Complete the breakingRecords function below.
def breakingRecords(scores):
    Hscore = 0
    Lscore = 0
    maxi = scores[0]
    mini = scores[0]
    for i in range(len(scores)):
        if(scores[i]>maxi):
            maxi = scores[i]
            Hscore+=1 
        if(scores[i]<mini):
            mini = scores[i]
            Lscore +=1
    return Hscore, Lscore 