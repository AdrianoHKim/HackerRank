import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)  # textwrap.fill : 'cut' the string in max_width size


if __name__ == '__main__':
    string, max_width = input('Type the string: '), int(input('Type the length of the results: '))
    result = wrap(string, max_width)
    print(result)
