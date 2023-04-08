x, y, z = str(input('Expression: ')).split()
x = int(x)
y
if y == '+':
    print(float(x + z))
elif y == '-':
    print(float(x - z))
elif y == '*':
    print(float(x * z))
elif y == '/':
    print(float(x / z))
    if z == 0:
