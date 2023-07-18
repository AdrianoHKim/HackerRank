"""
Task:

You are given an integer, n .
Your task is to print an alphabet rangoli of size n .
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""
def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(size)]
    items = list(range(size))
    items = items[:-1] + items[::-1]
    for i in items:
        temp = data[-(i + 1):]
        row = temp[::-1] + temp[1:]
        print("-".join(row).center(n * 4 - 3, "-"))


if __name__ == '__main__':
    n = int(input('Digit a number (1-27): '))
    print_rangoli(n)
