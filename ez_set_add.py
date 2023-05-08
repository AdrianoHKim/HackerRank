""" Task

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided
to count the total number of distinct country stamps in her collection.
She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.

Input Format

The first line contains an integer N, the total number of country stamps.
The next  lines contains the name of the country where the stamp is from.

Constraints
0 < n < 1000

Output Format

Output the total number of distinct country stamps on a single line.
"""

if __name__ == '__main__':
    n = int(input())  # read the number of country stamps
    stamps = set()  # create an empty set to store distinct stamps,
                    # to test here, type the countries(same as n)

    # read the names of country stamps and add them to the set
    for i in range(n):
        country = input().strip()
        stamps.add(country)

    # print the number of distinct country stamps
    print(len(stamps))
