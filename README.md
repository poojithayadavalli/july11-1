# Queue

You are given a square grid with some cells open (.) and some blocked (X). Your playing piece can move along any row or column

until it reaches the edge of the grid or a blocked cell. Given a grid, a start and an end position, 

determine the number of moves it will take to get to the end position.

INPUT FORMAT:

-The first line contains an integer n, the size of the array grid.

-Each of the next n lines contains a string of length n.

-The last line contains four space seperatedintegers, startX, startY, goalX, goalY

Output Format:

Print an integer denoting the minimum number of steps required to move the castle to the goal position.

Sample Input:
3
.X.
.X.
...
0 0 0 2

Sample Output

3

Explanaiton

Here is a path that one could follow in order to reach the destination in 3 steps:
(0,0) -> (2,0) -> (2,2) ->(0,2)
