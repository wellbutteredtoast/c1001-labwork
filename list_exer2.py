#ListExercise2.py

#contains a bug which must be fixed
def exer2():
    intArr = [0]*7
    for i in range(len(intArr)-1, -1, -1):
        intArr[i] = len(intArr) - 1 - i
    for i in range(0, len(intArr)+1):
        print(intArr[i], end=" ")
    print() 

exer2()