def Vector(a):
    b = []
    b.append(-1)
    for i in a:
        b.append(int(i))
    return b


def EleminList(e, l):
    flag = 0
    for item in l:
        flag = 0
        if (type(e) is int) and (type(item) is int):
            if e == item:
                return True
        elif (type(e) is tuple) and (type(item) is tuple):
            if len(e) != len(item):
                continue
            else:
                for i in e:
                    for j in item:
                        if i == j:
                            flag += 1
            if flag == len(e):
                return True
    return False


def NBP(g):
    leng = 1
    Cycle = []
    for elem in g:
        n = 0
        for i in range(1, len(elem)):
            st = elem[i]
            an = (elem[i])
            while elem[st] != elem[i]:
                an = (an, elem[st])
                st = elem[st]
            if EleminList(an, Cycle) is False:
                Cycle.append(an)
                n += 1
        leng *= n
    return Cycle, leng


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
            print(NBP(dt))
        except:
            break
