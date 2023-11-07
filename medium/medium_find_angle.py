"""
A
 |\
 | \
 |  \
 | / \
 |/)x_\ C
B

ABC is a right triangle, 90° at B.
Therefore, /_ ABC = 90°.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB  and BC.
Your task is to find /_ MBC (angle x°, as shown in the figure) in degrees.

Input Format

The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints
- 0 < AB <= 100
- 0 < BC <= 100
- Lengths AB  and BC are natural numbers.

Note: Round the angle to the nearest integer.

"""

import math

# Input the length of side AB
ab = int(input())

# Input the length of side BC
bc = int(input())

# Calculate the arctangent of the ratio ab/bc using math.atan2
result = math.atan2(ab, bc)

# Define the degree symbol as an ASCII character
degree_symbol = chr(176)

# Convert radians to degrees, round to the nearest integer, and add the degree symbol
angle_in_degrees = round(math.degrees(result))

# Print the angle with the degree symbol
print(f'{angle_in_degrees}{degree_symbol}')
