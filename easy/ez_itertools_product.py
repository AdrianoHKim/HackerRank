from itertools import product
A = input().split()       # you can input "1 2" here to see the result
A = list(map(int, A))
B = input().split()       # you need to input "3 4" here to see the result :D
B = list(map(int, B))
output = list(product(A, B))
for i in output:
    print(i, end=" ")
