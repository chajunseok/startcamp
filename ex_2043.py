Numbers = list(map(int,input().split()))
a = 0
b = 999 - Numbers[1]

if Numbers[1] <= Numbers[0]:
    for i in range(Numbers[1],1000):
        if i != Numbers[0]:
            a += 1
        elif i == Numbers[0]:
            print(a)

elif Numbers[1] > Numbers[0]:
    for i in range(0,1000):
        if i != Numbers[0]:
            a += 1
        elif i == Numbers[0]:
            print(a+b)