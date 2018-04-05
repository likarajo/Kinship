import matplotlib.pylab as pl
import json
import os

def plot(mined_data_file):
    #print('Plotting data....')
    f = open(mined_data_file,'r')
    words, counts = zip(*json.load(f))
    f.close()
    os.remove(mined_data_file)
    pl.figure(1)
    x = range(len(words))
    pl.xticks(x, words, rotation=45)
    pl.plot(x, counts, 'xr')
    #print('Plot prepared!')
    #pl.savefig('plot.png')
    #print('Plot saved in plot.png file!')
    pl.show()
