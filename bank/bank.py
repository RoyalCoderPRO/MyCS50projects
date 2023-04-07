x = input('Greeting: ').lower().split()
if 'hello' in x[0]:
    print('$0')
elif 'h' == x[0].split():
    print('$20')
else:
    print('$100')