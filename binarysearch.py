# _*_ coding:utf-8 _*_


def BinaryInsert(a, x, r=0, q=None):
    mid = (q + r) // 2
    if r < 0:
        raise ValueError('r must be non-positive nubmer!')
    while r < q:
        if a[q] < x:
            return q + 1
        if a[r] > x:
            return 0
        mid = (r + q) // 2
        if x <= a[mid]:
            q = mid
        else:
            r = mid + 1
    return r

if __name__ == "__main__":
    n = int(input())
    tmp = input().split(' ')
    a = []
    for i in tmp:
        a.append(int(i))
    target = int(input())
    print(BinaryInsert(a, target, 0, n - 1))
