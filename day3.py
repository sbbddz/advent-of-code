import collections

with open("day3.txt") as file:
    data = file.read().split("\n")
    data.pop()

bits = list(zip(*data))

digit_most_common = ''
digit_less_common = ''
for x in bits:
    col_data = collections.Counter(x)
    most_common = col_data.most_common()[0][0]
    less_common = col_data.most_common()[1][0]
    digit_less_common += less_common
    digit_most_common += most_common

print(int(digit_most_common, 2) * int(digit_less_common, 2))
