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
groceries_list = sorted(groceries)
for grocery in groceries_list:
    print(str(groceries[grocery]) + ' ' + grocery)
