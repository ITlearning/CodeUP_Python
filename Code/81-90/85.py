d,e,f = input().split()

a = int(d)
b = int(e)
c = int(f)

total = ((a*b*c)/8)/1024/1024

print(format(total, ".2f"), "MB")