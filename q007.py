import datetime

dnow = datetime.date(1964, 10, 10)
dend = datetime.date(2020, 7, 24)
while dend >= dnow:
    dnow += datetime.timedelta(days=1)
    snow = format(int(dnow.strftime('%Y%m%d')), 'b')
    if snow == snow[::-1]:
        print(snow, dnow)
