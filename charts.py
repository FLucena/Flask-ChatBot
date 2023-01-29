# pylab is a module in matplotlib

import numpy as np
import pylab as pl

ds = np.random.normal(5.0, 3.0, 100)

pl.hist(ds)

pl.xlabel('ds')
pl.show()
