

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if (grades[i]>37):
            if ((grades[i]%5) != 0):
                if (5-(grades[i]%5)<3):
                    grades[i] = grades[i] + 5-(grades[i]%5)
    return grades  