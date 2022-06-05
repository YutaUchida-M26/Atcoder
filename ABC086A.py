a = list(map(int, input().split()))

b = a[0] * a[1]

if b % 2 == 0:
    print("Even")
else:
    print("Odd")