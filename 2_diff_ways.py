#!/usr/bin/python

########################### 1st way #######################1

import math

class Rahul_math:

    def __init__(self, value):
        self.value = value

    def squart(self):
        try:
            x = int(input('Enter Value(1): '))
            value = math.sqrt(x)
            return value
        except ValueError:
            print('Entered Value is not a number, please enter a valid number.')
            return 'Exit 1'

arith_instance = Rahul_math(0)     #Need to creat instance for this class "Rahul_math"
print(arith_instance.squart())

########################### 1st way END #######################1

########################### 2nd way #######################2

import math
from math import sqrt

try:
    x2 = int(input('Enter Value(2): '))
    value2 = sqrt(x2)
    print(value2)
except ValueError:
    print('Entered Value is not a number, please enter a valid number.')
    print('Exit 2')

####################### 2nd way End ###############2

####### If module is not in script dir ######Start##########3
'''

import sys
sys.path.append("Paste hear you module location")
import # import your required module

'''
####### If module is not in script dir ######END##########3

