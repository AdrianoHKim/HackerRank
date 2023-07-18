""" Task

Dr. John Wesley has a spreadsheet containing a list of student's ID, marks, class and name
Your task is to help Dr. Wesley calculate the average marks of the students.
average = sum of all marks/total of students

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer N , the total number of students.
The second line contains the names of the columns in any order.
The next N  lines contains the marks,ID ,  name and Class, under their respective column names.
Output Format

Print the average marks of the list corrected to 2 decimal places.

Sample Input

TESTCASE 01

5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6
Sample Output

TESTCASE 01

78.00
"""

from collections import namedtuple


#  This code creates a list of Student objects using a list comprehension,
#  and then extracts the MARKS attribute from each object using another list comprehension.
#  Finally, it calculates the average marks and prints the result to two decimal places.

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)

marks = [int(student.MARKS) for student in [Student._make(input().split()) for _ in range(n)]]
print("{:.2f}".format(sum(marks)/n))
