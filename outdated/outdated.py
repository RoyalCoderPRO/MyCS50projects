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
    x = input('Put your goddamn date here: ')
    try:
        if '/' in x:
            m, d, y = x.strip().split('/')
            assert int(day) <= 31
            d, m = d.zfill(2), m.zfill(2)
            print(f'{y}-{m}-{d}')
            break
        elif ',' in x:
            m, d, y = x.strip().split()
            day = d.replace(',','')
            assert int(day) <= 31
            m = months.index(m)+1
            day, m = str(day).zfill(2), str(m).zfill(2)
            print(f'{y}-{m}-{day}')
            break
    except (AssertionError, ValueError):
        pass

