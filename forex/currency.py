from forex_python.converter import CurrencyRates
import datetime
from datetime import timedelta, date


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


c = CurrencyRates()
start_date = date(2021, 1, 1)
end_date = date(2021, 1, 13)
for single_date in daterange(start_date, end_date):
    date_obj = datetime.datetime(single_date.year, single_date.month, single_date.day, 18, 36, 28)
    # print(single_date.strftime("%Y-%m-%d"))
    print(date_obj.timestamp(), c.get_rate('USD', 'TRY', date_obj))