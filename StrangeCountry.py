x = input()
y = input()
z = ""
for i in range(len(x)):
    if int(x[i]) != int(y[i]):
        z += '0'
    else:
        z += '1'
print(z)
