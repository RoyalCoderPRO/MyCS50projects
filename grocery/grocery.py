groceries = {}
while True:
    try:
        x = input().upper()
        i = 1
        if x in groceries:
            i += 1
        groceries[x] = i
    except EOFError:
        break
groceries = sorted(groceries)
for grocery in groceries:
    print(grocery)
