# Nathan Davis, timeloop.py, 5/26/2020
from time import sleep


i = 0
for i in range(1,20,1):
    print(chr(48+i))
    sleep(2)
    i = 1 + i