# _*_ coding:utf-8 _*_
data = input().split(' ')
m = int(data[0])
n = int(data[1])
f = int(data[2])
ls = []
for i in range(m):
    lst = input().split(' ')
    ls.append(lst)
if f == 0:
    for l in ls:
        print(' '.join(l[::-1]) + ' ')
else:
    for i in range(m):
        print(' '.join(ls[m-1-i]) + ' ')