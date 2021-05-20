d = [[0 for j in range(10)] for i in range(10)]

for i in range(10) :
    a = [int(x) for x in input().split()]
    for j in range(10) :
        d[i][j] = a[j-1]

X = 2
Y = 2

while X <= 10 or Y <= 10 or X > 0 or Y > 0 :
    if(d[X][Y+1] == 2) :
        d[X][Y+1] = 9
        break
    elif(d[X+1][Y] == 2) :
        d[X+1][Y] = 9
        break

    if(d[X][Y+1] == 1) :
        if(d[X+1][Y] != 1) :
            X += 1
            d[X][Y] = 9
    else :
        Y += 1
        d[X][Y] = 9

for i in range(10) :
    for j in range(10) :
        print(d[i][j], end=' ')
    print()