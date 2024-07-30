<b>TASK</b><br />
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles. (i.e. Q3 - Q1)<br /><br />

Given an array, <i>values</i>, of <i>n</i> integers and an array, <i>freqs</i>, representing the respective frequencies of <i>values</i>'s elements, construct a data set, <i>S</i>, where each <i>values[i]</i> occurs at frequency <i>freqs[i]<i>.<br />
Then calculate and print <i>S</i>'s interquartile range, rounded to a scale of 1 decimal place. (i.e. 12.3)<br /><br />

Tip: Be careful not to use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.<br /><br />

<b>EXAMPLE</b>
values = [1, 2, 3]<br />
freqs = [3, 2, 1]<br /><br />

Apply the frequencies to the values to get the expanded array.<br />
S = [1, 1, 1, 2, 2, 3]<br />
Here, we retrieve:<br />
left = [1, 1, 1]<br />
right = [2, 2, 3].<br /><br />

The median on the left half: Q1 = 1.0.<br />
For the right half: Q3 = 2.0.<br />

Print the differene to one decimal place:<br />
Q3 - Q1 = 2.0 - 1.0 = 1. <br /><br />

Therefore print 1.0.<br /><br />

<b>FUNCTION DESCRIPTION</b><br />
interQuartile has the following parameters:<br />
- int values[n]: array of integers<br />
- int freqs[n]: values[i] occurs freqs[i] times in the array to analyze<br />
Prints:<br />
- float: interquartile range to 1 place after the decimal<br /><br />

<b>INPUT FORMAT</b><br />
The first line contains an integer, n, the number of elements in arrays values and freqs.<br />
The second line contains n space-separated integers describing the elements of array 'values'.<br />
The third line contains n space-separated integers describing the elements of array 'freqs'.<br /><br />

<b>CONSTRAINTS</b><br />
- 5 <= n <= 50<br />
- 0 < values[i] <= 100<br />
- 0 < sigma(n-1;i=0) s.t. {freqs[i]} <= 10^3<br />
- The number of elements in S is equal to sigma(freqs).<br /><br />

<b>OUTPUT FORMAT</b><br />
Print the interquartile range for the expanded data set on a new line.<br />
Round the answer to a scale of 1 decimal place (i.e. 12.3 format).<br /><br />