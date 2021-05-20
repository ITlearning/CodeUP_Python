c,d = input().split()
a = int(c)
b = int(d)
k = [[0 for i in range(a)] for j in range(b)]

cnt = int(input())

for i in range(cnt) :
    l,d,x,y = input().split()
    if int(d) == 0 :
        for j in range(int(l)) :
            k[(int(y)+j)-1][int(x)-1] = 1
    elif int(d) == 1 :
        for m in range(int(l)) :
            k[int(y)-1][(int(x)+m)-1] = 1

for i in range(a) :
    for j in range(b) :
        print(k[j][i], end=' ')
    print()