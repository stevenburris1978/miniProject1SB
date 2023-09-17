# https://pypi.org/project/yfinance/

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

msft = yf.Ticker("MSFT")

dataOne = yf.download("PZZA", start="2023-08-17", end="2023-08-31")

print(dataOne['Close'])

z = (dataOne['Close'])

y = np.array(z)

plt.plot(y, 'red')
plt.title('Trading Days Aug 17th - Aug 30th')
plt.ylabel('Papa Johns Closing Price')
plt.savefig('Charts\chart1.png')
plt.show()

dataTwo = yf.download("AAPL", start="2023-08-17", end="2023-08-31")

print(dataTwo['Close'])

u = (dataTwo['Close'])

w = np.array(u)

plt.plot(w, 'bs')
plt.title('Trading Days Aug 17th - Aug 30th')
plt.ylabel('Apple Closing Price')
plt.savefig('Charts\chart2.png')
plt.show()

dataThree = yf.download("LUV", start="2023-08-17", end="2023-08-31")

print(dataThree['Close'])

t = (dataThree['Close'])

v = np.array(t)

plt.plot(v, 'red')
plt.plot(v, 'o')
plt.title('Trading Days Aug 17th - Aug 30th')
plt.ylabel('Southwest Airline Closing Price')
plt.savefig('Charts\chart3.png')
plt.show()

dataFour = yf.download("TSLA", start="2023-08-17", end="2023-08-31")

print(dataFour['Close'])

r = (dataFour['Close'])

s = np.array(r)

plt.plot(s, 'red')
plt.plot(s, 'o')
plt.title('Trading Days Aug 17th - Aug 30th')
plt.ylabel('Tesla Closing Price')
plt.savefig('Charts\chart4.png')
plt.show()

dataFive = yf.download("AMZN", start="2023-08-17", end="2023-08-31")

print(dataFive['Close'])

o = (dataFive['Close'])

p = np.array(o)

plt.plot(p, 'red')
plt.plot(p, 'o')
plt.title('Trading Days Aug 17th - Aug 30th')
plt.ylabel('Amazon Closing Price')
plt.savefig('Charts\chart5.png')
plt.show()


