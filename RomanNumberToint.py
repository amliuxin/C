def Convert(s):
    sum = 0
    dt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
          'D': 500, 'M': 1000}
    for i in range(len(s)):
        val = dt[s[i]]
        if i == len(s) - 1 or dt[s[i + 1]] <= dt[s[i]]:
            sum += val
        else:
            sum -= val
    return sum

s = input()
print(Convert(s))
