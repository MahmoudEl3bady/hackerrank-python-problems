#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    
   


    if int(n)%2!=0:
        print('Weird')
    elif int(n)%2==0 and 2<=n<=5:
        print('Not Weird')
    elif int(n)%2==0 and 5<=n<=20 :
        print('Weird')
    elif int(n)%2==0 and int(n)>20 :
        print('Not Weird')
