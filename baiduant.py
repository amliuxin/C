# _*_ coding:utf-8 _*_
num = int(raw_input())
for _ in range(num):
    [l, n] = raw_input().split()
    dist = [int(x) for x in raw_input().split()]
    mind = 0
    for item in dist:
        tp = min(item, l - item)
        if tp > mind:
            mind = tp
    redist = [l - x for x in dist]
    maxd = max(max(dist), max(redist))
    print mind, maxd
