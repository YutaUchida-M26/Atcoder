a = int(input())
b = list(map(int, input().split()))
judge = 0
cnt = 0
while True:
    for n in b:
        if n % 2 == 1:
            judge = 1
            break
    if judge == 0:
        cnt += 1
        for i in range(len(b)):
            b[i] /= 2
    else:
        break

print(cnt)