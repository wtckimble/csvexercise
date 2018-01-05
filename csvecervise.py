import csv
from datetime import datetime

path = "C:\\Users\\Kimble\\Documents\\Python Exercise\\google_stock_data.csv"
file = open(path, newline = '')
reader = csv.reader(file)

#skip header
header = next(reader)

data = []
for row in reader:
        #row = [Date, Open, High, Low, Close, Volume, Adj.Close]
        date = datetime.strptime(row[0], '%m/%d/%Y')
        open_price = float(row[1])
        high_price = float(row[2])
        low_price = float(row[3])
        close_price = float(row[4])
        volume = int(row[5])
        adj_close = float(row[6])

        data.append([date, open_price, high_price, low_price, close_price, volume, adj_close])

#calculate stock returns
returns_path = "C:\\Users\\Kimble\\Documents\\Python Exercise\\google_stock_returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Returns"])

for i in range(len(data) - 1):
        todays_row = data[i]
        todays_date = todays_row[0]
        todays_price = todays_row[-1]
        yesterdays_row = data[i+1]
        yesterdays_price = yesterdays_row[-1]

        daily_returns = (todays_price - yesterdays_price) / yesterdays_price
        formatted_date = todays_date.strftime('%m/%d/%Y')
        writer.writerow([formatted_date, daily_returns])