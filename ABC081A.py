a = int(input())
cnt = 0

while True:
    if a == 0:
        break
    if a % 2 == 1:
        cnt += 1
        a /= 10
        a = int(a)
    else:
        a /= 10

print(cnt)