from iexfinance.stocks import Stock
from datetime import datetime
from iexfinance.stocks import get_historical_data
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_intraday

tsla = Stock('TSLA')
tsla.get_price()

batch = Stock(["TSLA", "AAPL"])
batch.get_price()

start = datetime(2017, 1, 1)
end = datetime(2018, 1, 1)
df = get_historical_data("TSLA", start, end)
df = get_historical_data("TSLA", start, end, output_format='pandas')
df.plot()
plt.show()
