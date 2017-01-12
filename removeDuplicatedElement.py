n = int(input())
a = input().split(' ')
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            n -= 1
        else:
            i = j
            break
print(n)
