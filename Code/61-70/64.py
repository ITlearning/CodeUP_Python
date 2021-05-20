c,d,e = input().split()
a = int(c)
b = int(d)
c = int(e)

print((a if a < b else b) if ((a if a < b else b) < c)else c)