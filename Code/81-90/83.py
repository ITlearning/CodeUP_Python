d,e,f = input().split()
a = int(d)
b = int(e)
c = int(f)
cnt = 0
for i in range(a) :
    for j in range(b) :
        for k in range(c) :
            print(i,j,k, sep= ' ')
            cnt += 1

print(cnt)
