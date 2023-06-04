import matplotlib.pyplot as plt
import cv2
import numpy as np


im = cv2.imread('reference_black_edge_10.png')
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# plot histogram with 255 bins
b, bins, patches = plt.hist(vals, 255)

np.sum(b[100:]*bins[101:])/np.sum(b[100:])

treshold = round(len(bins)/1.7)

#b_f = b
#b_f[b_f < np.average(b_f)*1.3] = 0
av_max = bins[treshold+np.argmax(b[treshold:])]#np.sum(b_f[50:]*bins[51:])/np.sum(b_f[50:])
plt.vlines(av_max, 0, np.max(b), color="orange", linestyles="--")

#b_f = b
#b_f[b_f < np.average(b_f)*4] = 0
av_min = bins[np.argmax(b[:treshold])] #np.sum(b_f[:50]*bins[:50])/np.sum(b_f[:50])
plt.vlines(av_min, 0, np.max(b), color="orange", linestyles="--")

plt.title(str(round(av_min, 1)) + ", " + str(round(av_max, 1)))
plt.xlim([0,255])
plt.show()
