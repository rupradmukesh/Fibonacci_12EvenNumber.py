def Fibonacci(First, Second):
    for X in range(36):
        if( X == 0 ):
            Next = 1
        else:
            Next = First + Second
            First = Second
            Second = Next
        if(Next%2 == 0):
            print (Next)


A = 1
B = 1
Fibonacci(A, B)
