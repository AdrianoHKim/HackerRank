"""Task
You are given a complex .
Your task is to convert it to polar coordinates.

Input Format
A single line containing the complex number.
Note: complex() function can be used in python to convert the input as a complex number.

Constraints
Given number is a valid complex number

Output Format
Output two lines:
The first line should contain the value of r .
The second line should contain the value of θ."""

from cmath import sqrt, phase
c = complex(input())

print(sqrt(pow(c.real, 2)+pow(c.imag, 2)).real)
print(phase(complex(c.real, c.imag)))
