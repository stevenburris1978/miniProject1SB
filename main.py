# https://pypi.org/project/yfinance/

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

msft = yf.Ticker("MSFT")

data = yf.download("PZZA", start="2023-08-17", end="2023-08-31")

print(data['Close'])

z = (data['Close'])

y = np.array(z)

plt.plot(y, 'red')
plt.show()

b = [2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18]

a = np.array(b)

plt.plot(a, 'red')
plt.savefig('Charts\chart1.png')
plt.show()

plt.plot(a, 'bs')
plt.savefig('Charts\chart2.png')
plt.show()

plt.plot(a, 'red')
plt.plot(a, 'o')
plt.title('Last 10 Trading Days')
plt.ylabel('Stock Closing Price')
plt.savefig('Charts\chart3.png')
plt.show()

plt.plot(a, 'red')
plt.plot(a, 'o')
plt.title('Last 10 Trading Days')
plt.ylabel('Stock Closing Price')
plt.savefig('Charts\chart4.png')
plt.show()

plt.plot(a, 'red')
plt.plot(a, 'o')
plt.title('Last 10 Trading Days')
plt.ylabel('Stock Closing Price')
plt.savefig('Charts\chart5.png')
plt.show()
