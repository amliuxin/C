n = int(input())
a = input().split(' ')
for i in range(n):
    f = 0
    for j in range(n):
        if a[i] == a[j]:
            f += 1
    if f == 1:
        print(a[i])
        break
