#!/bin/python3
import math
import os
import random
import re
import sys

# Function responsible for modulating quartile calculations.
def quartile_calculation(bounds):
    if (len(bounds) % 2 == 0):
        # Even Set Count
        q_upper_index = int(len(bounds) / 2)
        q_lower_index = q_upper_index - 1
        quartile = (float(bounds[q_upper_index]) + float(bounds[q_lower_index])) / 2
    elif (len(bounds) % 2 == 1):
        # Odd Set Count
        q_index = int(len(bounds) / 2)
        quartile = float(bounds[q_index])
     
    return quartile

def interQuartile(values, freqs):
    data_size = len(values)
    
    # Generate S array
    s = []
    for i in range(0, data_size):
        value = values[i]
        frequency = freqs[i]
        # For each frequency, append to list that many times.
        for j in range(0, frequency):
            s.append(value)
            
    s.sort()
    s_size = len(s)
    
    # Even Case
    if (s_size % 2 == 0):
        middle_index = int(s_size / 2)
        lower_bound = s[:middle_index]
        upper_bound = s[middle_index:]
        
        # Calculate Q1
        q1 = quartile_calculation(lower_bound)
        
        # Calculate Q3
        q3 = quartile_calculation(upper_bound)
        
    # Odd Case
    if (s_size % 2 == 1):
        middle_index = int(s_size / 2)
        lower_bound = s[:middle_index]
        upper_bound = s[(middle_index + 1):]
        
        # Calculate Q1
        q1 = quartile_calculation(lower_bound)
       
        # Calculate Q3
        q3 = quartile_calculation(upper_bound)
    
    iqr = q3 - q1
    print(float(iqr))
    
if __name__ == '__main__':
    # Uncomment for original driver logic
    #n = int(input().strip())
    #val = list(map(int, input().rstrip().split()))
    #freq = list(map(int, input().rstrip().split()))

    # Comment when using original driver logic
    val = [1, 2, 3]
    freq = [3, 2, 1]
    interQuartile(val, freq)
    