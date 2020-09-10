
def camelCase(s):
    count=1
    for i in range(len(s)):
        if (s[i].isupper()):
            count+=1
    return count   