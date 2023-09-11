import numpy as np
import matplotlib.pyplot as plt

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
