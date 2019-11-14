import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def plot():
    x = [17.5, 9.8, 5.88, 6.4, 21.8, 28.0, 9.9, 8.0, 26.0, 5.4, 5.3, 7.5, 5.8,
         8.7, 9.0, 5.4, 26.0, 18.9, 8.7, 18.0, 16.5, 9.7, 9.5, 25.0, 58.0, 147.0,
         5.4, 5.4, 5.4, 6.8, 5.5, 4.2, 18.0, 17.5, 18.0, 5.69, 5.55, 19.88, 95.0,
         15.9, 35.6, 9.8, 23.75, 24.51, 18.8, 9.0, 20.0, 15.0, 7.3, 7.3, 4.9, 5.66,
         9.85, 15.35, 15.9, 28.0, 7.99, 13.7, 10.0, 27.0, 8.65, 65.0, 39.0, 9.9,
         5.18, 5.4, 16.5, 11.8, 16.8, 13.5, 18.9, 69.0, 59.0, 23.9, 150.0, 13.5,
         60.0, 18.0, 11.2, 25.0, 9.0, 7.25, 24.99, 6.08, 3.6, 7.1, 11.5, 17.5,
         29.0, 21.0, 8.5, 198.0]
   # print len(x)
    total = 0
    for i in range(len(x)):
        total += x[i]
   # print total
    avr = total/len(x)
   # print avr
    y = 0
    for i in range(len(x)):
        y += np.square(x[i]-avr)
    sd = np.sqrt(y/len(x))
    #print sd

    plt.figure(1)
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
    z = mlab.normpdf(bins, avr, sd)
    plt.plot(bins, z, '--')
    plt.axis([0, 200, 0, 0.1])
    #print "搜本店"
    return plt

def main():
    plott = plot()
    x =plott.figure()
    x.show()

if __name__ == '__main__':
    main()
