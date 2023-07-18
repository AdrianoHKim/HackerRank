"""
Task

You are given a string s
Your task is to print all possible combinations, up to size k , of the string in lexicographic sorted order.

Input Format

A single line containing the string s and integer value k separated by a space.

Constraints
0 < k <=len(s)

The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  s on separate lines.

Sample Input : HACK 2

Sample output:
A
C
H
K
AC
AH
AK
CH
CK
HK
"""

from itertools import combinations


def print_combinations(s, k):
    # Generate all combinations up to size k
    all_combinations = []
    for r in range(1, k + 1):
        all_combinations.extend(combinations(sorted(s), r))

    # Sort combinations in the desired order
    all_combinations.sort(key=lambda x: (len(x), x))

    # Print combinations
    for combination in all_combinations:
        print(''.join(combination))


# Read input string and value of k
s, k = input().split()

# Call the function with the provided input
print_combinations(s, int(k))
