import requests
from datetime import datetime
import time

ticket = input("Enter ticket symbol: ")
from_date = input("Enter from date (yyyy-mm-dd): ")
to_date = input("Enter to date (yyyy-mm-dd): ")

from_datetime = datetime.strptime(from_date, "%Y-%m-%d")
to_datetime = datetime.strptime(to_date, "%Y-%m-%d")

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticket}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

content = requests.get(url, headers=headers).content
with open(f"{ticket}.csv", "wb") as file:
    file.write(content)