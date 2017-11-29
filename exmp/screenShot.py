Created on Wed Nov 29 15:26:30 2017

@author: bhadana
"""

from mss.windows import MSS as mss

sct = mss()
filename = sct.shot(mon=2)
print(filename)
