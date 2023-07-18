""" The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container, but the only difference
is that a defaultdict will have a default value if that key has not been set yet.
If you didn't use a defaultdict you'd have to check to see if that key exists,
and if it doesn't, set it to what you want.
"""


from collections import defaultdict

n, m = map(int, input().split())

a = defaultdict(list)
for i in range(1, n + 1):
    a[input()].append(i)

for i in range(1, m + 1):
    key = input()
    if len(a[key]) > 0:
        print(" ".join(str(c) for c in a[key]))
    else:
        print(-1)
