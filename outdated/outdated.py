months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    x = input()
    if '/' in x:
        m, d, y = x.split('/')
        d, m = d.zfill(2), m.zfill(2)
        print(f'{y}-{m}-{d}')
    elif ',' in x:
        
