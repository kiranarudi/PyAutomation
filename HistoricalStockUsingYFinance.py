import yfinance as yf
import pandas as pd

ticket = input("Enter ticket symbol: ")
from_date = input("Enter from date (yyyy-mm-dd): ")
to_date = input("Enter to date (yyyy-mm-dd): ")

# Download data using yfinance
data = yf.download(ticket, start=from_date, end=to_date)

# Save the data to CSV
data.to_csv(f"{ticket}.csv")

print(f"Data saved to {ticket}.csv")
