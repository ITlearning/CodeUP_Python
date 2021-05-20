d = [[0 for j in range(10)] for i in range(10)]

for i in range(10) :
    a = [int(x) for x in input().split()]
    for j in range(10) :
        d[i][j] = a[j]

X = 0
Y = 1
while True :
    if d[X][Y+1] == 0 :
        Y += 1
        d[X][Y] = 9
    elif d[X][Y+1] == 1 :
        if d[X+1][Y] == 0 :
            X += 1
            d[X][Y] = 9
        elif d[X+1][Y] == 1:
            break
        else :
            X += 1
            d[X][Y] = 9
            break
    elif d[X][Y+1] == 2 :
        Y += 1
        d[X][Y] = 9
        break

    if X == 9 or Y == 9 :
        break

for i in range(10) :
    for j in range(10) :
        print(d[i][j], end=' ')
    print()