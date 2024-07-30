<b>TASK</b><br />
Given an array, <i>arr</i>, of <i>n</i> integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e. 12.3 format). An error margin of +/-0.1 will be tolerated for the standard deviation.<br /><br />

<b>EXAMPLE</b><br />
arr = [2, 5, 2, 7, 4]<br /><br />
The sum of the array values is 20 and there are 5 elements. The mean is 4.0.<br />
Subtract the mean from each element, square each result, and take their sum.<br />
(2 - 4)^2 = 4<br />
(5 - 4)^2 = 1<br />
(2 - 4)^2 = 4<br />
(7 - 4)^2 = 9<br />
(4 - 4)^2 = 0<br />
Their sum is 18. Take the square root of 18/5 to get <b>1.7</b>, the standard deviation.<br /><br />

<b>FUNCTION DESCRIPTION</b><br />
stdDev has the following parameters:<br />
- int arr[n]: an array of integers<br /><br />

<b>Prints:</b><br />
- float: the standard deviation to 1 place after the decimal<br /><br />

<b>Input Format</b><br />
The first line contains an integer, <i>n</i>, denoting the size of arr.<br />
The second line contains <i>n</i> space-separated integers that describe <i>arr</i>.<br /><br />

<b>CONSTRAINTS</b><br />
- 5 <= n <= 100<br />
- 0 < arr[i] <= 10^5<br /><br />

<b>OUTPUT FORMAT</b><br />
Print the standard deviation on a new line, rounded to a scale of 1 decimal place (i.e. 12.3 format).<br />
