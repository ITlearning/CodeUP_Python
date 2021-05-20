e,f,g,h = input().split()

a = int(e)
b = int(f)
c = int(g)
d = int(h)

for i in range(d-1) :
    a *= b
    a += c

print(a)