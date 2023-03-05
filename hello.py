def calcy(num1,num2):
    num3 = int(num1) + int(num2)
    return num3
x, y = input('Input the numbers you want to have added: ').split()
print(calcy(x,y))