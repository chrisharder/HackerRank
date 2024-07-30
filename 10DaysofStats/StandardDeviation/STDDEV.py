#!/bin/python3
import math
from msilib import sequence
import os
import random
import re
import sys

def stdDev(arr):
    # First finding mean of provided array | O(n) Time Complexity
    arr_sum = 0.0
    arr_len = len(arr)
    for item in arr:
        arr_sum = item + arr_sum
    
    arr_mean = float(arr_sum) / float(arr_len)
    
    # Performing (i - arr_len)^2 for Squared Distance | O(n) Time Complexity
    sqrd_distance_sum = 0.0
    for item in arr:
        sqrd_distance = item - arr_mean
        sqrd_distance = sqrd_distance * sqrd_distance
        sqrd_distance_sum = sqrd_distance + sqrd_distance_sum
   
    # Find square root and round to 1 decimal place
    sqrd_distance_mean = float(sqrd_distance_sum) / float(arr_len)
    std_dev = math.sqrt(sqrd_distance_mean)
    print(round(std_dev, 1))
    
if __name__ == '__main__':
    vals = [10, 40, 30, 50, 20]    

    #n = int(input().strip())
    #vals = list(map(int, input().rstrip().split()))
    stdDev(vals)