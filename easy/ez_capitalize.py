def solve(a):
    a = s.split(' ')
    for i in range(len(a)):  # the answer
        a[i] = a[i].capitalize()
    return ' '.join(a)


if __name__ == '__main__':
    s = 'derek random something'
    print(solve(s))  # just to show the result here
