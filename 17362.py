N = int(input())

N = N%8

if N == 1 :
    print(1)
elif N in [2,0] : print(2)
elif N in [3,7] : print(3)
elif N in [4,6] : print(4)
elif N == 5:
    print(5)