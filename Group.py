def Product(a, b):
    n = len(a)
    c = [-1]
    for i in range(1, n):
        c.append(a[b[i]])
    return c


def Inverse(a):
    n = len(a)
    v = [-1 for i in range(n)]
    for i in range(1, n):
        v[a[i]] = i
    return v


def Vector(a):
    b = []
    b.append(-1)
    for i in a:
        b.append(int(i))
    return b


def Generate(d):
    le = len(d)
    result = d[:]
    for i in range(le):
        for j in range(i, le):
            tmp1 = Product(d[i], Inverse(d[j]))
            tmp2 = Product(Inverse(d[i]), d[j])
            if (tmp1 in result) is False:
                result.append(tmp1)
            if (tmp2 in result) is False:
                result.append(tmp2)
    result.sort()
    return result


if __name__ == "__main__":
    while True:
        try:
            line = input().split(' ')
            m = int(line[1])
            dt = []
            for i in range(m):
                tmp = input().split(' ')
                tmp = Vector(tmp)
                dt.append(tmp)
            dt.sort()
            while dt != Generate(dt):
                dt = Generate(dt)
            print(len(dt))
            print(dt)
        except:
            break
