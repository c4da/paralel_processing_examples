# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:57:25 2019

@author: cada
"""

from concurrent.futures import ThreadPoolExecutor
from time import sleep
import math
 
def function():
    vysl = list()
    for n in range(int(1e5)):
        vysl.append(math.sin(n))
    return vysl
 
pool = ThreadPoolExecutor(6)
 
future = pool.submit(function)
c_ = True
while c_:
    print("done = ", future.done())
    if future.done() == True:
        print(future.result())
        c_ = False
    sleep(1)