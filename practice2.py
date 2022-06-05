N, Q = (int(x) for x in input().split())
s = []
cnt = 0
for i in range(N):
    s.append(chr(ord("A") + i))


for j in range(N-1):
    print("? " + s[j] + " " + s[j+1])
    a = input()
    if a == ">" and j+2 < len(s):
        b = s[j]
        s[j] = s[j+2]
        s[j+2] = b
        cnt += 1
        print("? " + s[j] + " " + s[j+1])
        a = input()
        if a == ">":
            b = s[j]
            s[j] = s[j+1]
            s[j+1] = b
            cnt += 1
    
    if cnt == Q:
        break
        

print("!", end=' ')
print(*s, sep="")
        