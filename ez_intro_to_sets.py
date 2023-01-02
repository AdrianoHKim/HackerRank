""" A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College.
One day, she asked her student Mickey to compute the average of
all the plants with distinct heights in her greenhouse.

Formula used:  average = sum of distinct heights/total number of distinct heights

Function Description

Complete the average function in the editor below.

average has the following parameters:

int arr: an array of integers
Returns

float: the resulting float value rounded to 3 places after the decimal

Input Format

The first line contains the integer, N , the size of arr .
The second line contains  the N space-separated integers, arr[i] .

constraints
0 < N <= 100
"""


def average(array):
    # your code goes here
    sum_array = sum(set(array))
    len_array = len(set(array))
    output = sum_array / len_array
    return output


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
