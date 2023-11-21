"""
You are given n  words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:
1<= n <= 10**5
The sum of the lengths of all the words do not exceed 10**6
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, n .
The next  lines each contain a word.

Output Format

Output  2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according
to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
Explanation

There are 3 distinct words. Here, "bcdef" appears twice in the input at the
first and last positions. The other words appear once each.
The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

"""

from collections import OrderedDict

# Define a function to calculate word occurrences
def word_occurrences(n, words):
    # Use an OrderedDict to maintain the order of word appearance
    word_count = OrderedDict()

    # Count occurrences of each word in the input list
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Calculate the number of distinct words
    distinct_words_count = len(word_count)

    # Create a list of word occurrences according to their appearance in the input
    occurrences_list = list(word_count.values())

    # Output the results
    print(distinct_words_count)
    print(" ".join(map(str, occurrences_list)))

# Input reading
n = int(input())  # Read the number of words
words = [input().strip() for _ in range(n)]  # Read the words

# Output
word_occurrences(n, words)  # Call the function with the input data

