x, y, z = str(input('Expression: ')).split()
x = int(x)
y = int(z)
if y == '+':
    print(float(x + z))
elif y == '-':
    print(float(x - z))
elif y == '*':
    print(float(x * z))
elif y == '/':
    print(float(x / z))
