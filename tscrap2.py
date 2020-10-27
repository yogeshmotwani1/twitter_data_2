import os
import subprocess
import random, time, queue
import multiprocessing
multiprocessing.set_start_method('spawn')

from multiprocessing.managers import BaseManager
# command=['twint -s "@exidecare"  -o exidecare.csv --csv --limit 100','twint -s "@venkysindia"  -o venkys.csv --csv --limit 100']

company = ['H & R Johnson (India)','Jubiliant life sciences ltd','K raheja private limited','K raheja private limited','K raheja private limited']
handle = ['@HRJohnsonIndia','@jubiliantlifesci','@corpraheja','@inorbitmall','@shoppersstop']
print(len(company))
print(len(handle))
for i in range(0,len(company)):
    print(company[i]+" ---> "+handle[i])

for i in range(0,len(company)):
    cmd = subprocess.Popen('twint -s '+'"'+handle[i]+'" '+'-o '+'"'+company[i]+"#"+handle[i]+".csv "+'" '+'--csv '+'--limit 150000'+' -ho')
    cmd.communicate() 