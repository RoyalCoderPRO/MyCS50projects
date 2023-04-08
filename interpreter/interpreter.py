x, y, z = str(input('Expression: ')).split()
x = int(x)
z = int(z)
if y == '+':
    print(float(x + z))
elif y == '-':
    print(float(x - z))
elif y == '*':
    print(float(x * z))
elif y == '/':
    print(float(x / z))
