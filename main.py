# INF601VA - Advanced Programming in Python
# Steven Burris
# 09-16-2023
# *Mini Project 1SB*
# https://pypi.org/project/yfinance/

import pprint
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

pzza = yf.Ticker("PZZA")

hist = pzza.history(period="10d")

pprint.pprint(hist['Close'])

z = (hist['Close'])

y = np.array(z)

plt.plot(y, 'red')
plt.title('Last 10 Trading Days')
plt.ylabel('Papa Johns Closing Price')
plt.savefig('Charts\chart1.png')
plt.show()

aapl = yf.Ticker("AAPL")

dataTwo =aapl.history(period="10d")

pprint.pprint(dataTwo['Close'])

u = (dataTwo['Close'])

w = np.array(u)

plt.plot(w, 'bs')
plt.title('Last 10 Trading Days')
plt.ylabel('Apple Closing Price')
plt.savefig('Charts\chart2.png')
plt.show()

luv = yf.Ticker("LUV")

dataThree = luv.history(period="10d")

pprint.pprint(dataThree['Close'])

t = (dataThree['Close'])

v = np.array(t)

plt.plot(v, 'red')
plt.plot(v, 'o')
plt.title('Last 10 Trading Days')
plt.ylabel('Southwest Airline Closing Price')
plt.savefig('Charts\chart3.png')
plt.show()

amzn = yf.Ticker("AMZN")

dataFive = amzn.history(period="10d")

pprint.pprint(dataFive['Close'])

o = (dataFive['Close'])

p = np.array(o)

plt.plot(p, 'red')
plt.plot(p, 'o')
plt.title('Last 10 Trading Days')
plt.ylabel('Amazon Closing Price')
plt.savefig('Charts\chart4.png')
plt.show()

tsla = yf.Ticker("TSLA")

dataFour = tsla.history(period="10d")

pprint.pprint(dataFour['Close'])

r = (dataFour['Close'])

s = np.array(r)

plt.plot(s, 'red')
plt.plot(s, 'o')
plt.title('Tesla Last 10 Trading Days')
plt.ylabel('Closing Price')
plt.savefig('Charts\chart5.png')
plt.show()

# closing prices for Tesla Aug 17 2023 to Aug 31 trading days
dataSix = yf.download("TSLA", start="2023-08-17", end="2023-08-31")

pprint.pprint(dataSix['Close'])

r = (dataSix['Close'])

s = np.array(r)

plt.plot(s, 'red')
plt.plot(s, 'o')
plt.title('Tesla Trading Days 8-17-23 to 8-30-23')
plt.ylabel('Closing Price')
plt.savefig('Charts\chart6.png')
plt.show()


