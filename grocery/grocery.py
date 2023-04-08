x = {}
while True:
    try:
        x = input().upper()
        if x in groceries:

        else:
            groceries.append(x)
    except EOFError:
        break
groceries = sorted(groceries)
for grocery in groceries:
    print(grocery)
