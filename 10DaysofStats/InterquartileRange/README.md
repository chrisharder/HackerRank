TASK
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles. (i.e. Q3 - Q1)

Given an array, 'values', of <i>n</i> integers and an array, 'freqs', representing the respective frequencies of 'value''s elements, construct a data set, 'S', where each 'values[i]' occurs at frequency 'freqs[i]'.
Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place. (i.e. 12.3)

Tip: Be careful not to use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets. 

EXAMPLE
values = [1, 2, 3]
freqs = [3, 2, 1]

Apply the frequencies to the values to get the expanded array.
S = [1, 1, 1, 2, 2, 3]
Here, we retrieve:
left = [1, 1, 1]
right = [2, 2, 3].

The median on the left half: Q1 = 1.0.
For the right half: Q3 = 2.0.

Print the differene to one decimal place:
Q3 - Q1 = 2.0 - 1.0 = 1. 

Therefore print 1.0.

FUNCTION DESCRIPTION
interQuartile has the following parameters:
- int values[n]: array of integers
- int freqs[n]: values[i] occurs freqs[i] times in the array to analyze
Prints:
- float: interquartile range to 1 place after the decimal

INPUT FORMAT
The first line contains an integer, n, the number of elements in arrays values and freqs.
The second line contains n space-separated integers describing the elements of array 'values'.
The third line contains n space-separated integers describing the elements of array 'freqs'.

CONSTRAINTS
- 5 <= n <= 50
- 0 < values[i] <= 100
- 0 < sigma(n-1;i=0) s.t. {freqs[i]} <= 10^3
- The number of elements in S is equal to sigma(freqs).

OUTPUT FORMAT
Print the interquartile range for the expanded data set on a new line.
Round the answer to a scale of 1 decimal place (i.e. 12.3 format).