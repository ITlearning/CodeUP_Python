d,e,f = input().split()

a = int(d)
b = int(e)
c = int(f)
day = 1

while day%a != 0 or day%b != 0 or day%c != 0 :
    day += 1

print(day)
