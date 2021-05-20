e,f,g,h = input().split()

a = int(e)
b = int(f)
c = int(g)
d = int(h)

total = ((a*b*c*d)/8)/1024/1024
print(format(total, ".1f"), "MB")