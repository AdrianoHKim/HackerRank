""" A counter is a container that stores elements as dictionary keys,
 and their counts are stored as dictionary values.

Task

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N  number of customers who are willing to pay x amount of money only
if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains X , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the  desired by the customer and x,
the price of the shoe.

Constraints
0 < X < 10³
0 < N <= 10³
20 < x < 100
2 < shoe size < 20

Output Format

Print the amount of money earned by Raghu.
"""

from collections import Counter

X = input()
S = Counter(map(int, input().split()))
n = input()
N = int(n)
earnings = 0
for customer in range(N):
    size, x_i = map(int, input().split())
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i

print(earnings)
