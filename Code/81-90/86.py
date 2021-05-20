a = int(input())
i = 1
total = 0
while True :
    total += i
    i += 1
    if total >= a:
        break

print(total)