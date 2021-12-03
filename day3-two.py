import collections

with open("day3.txt") as file:
    data = file.read().split("\n")
    data.pop()


def get_oxygen(arr):
    data = arr[:]
    i = 0
    while(len(data) > 1):
        bits = list(zip(*data))

        col_data = collections.Counter(bits[i])
        most_common = col_data.most_common()[0]
        less_common = col_data.most_common()[1]

        if (most_common[1] == less_common[1]):
            data = list(filter(lambda x: int(str(x)[i]) == 0, data))
        else:
            data = list(filter(lambda x: int(str(x)[i]) != int(most_common[0]), data))
                
        i += 1

    return data[0]

def get_co2(arr):
    data = arr[:]
    i = 0
    while(len(data) > 1):
        bits = list(zip(*data))

        col_data = collections.Counter(bits[i])
        most_common = col_data.most_common()[0]
        less_common = col_data.most_common()[1]

        if (most_common[1] == less_common[1]):
            data = list(filter(lambda x: int(str(x)[i]) == 1, data))
        else:
            data = list(filter(lambda x: int(str(x)[i]) == int(most_common[0]), data))
                
        i += 1

    return data[0]

print(int(get_oxygen(data), 2))
print(int(get_co2(data), 2))
print(int(get_oxygen(data), 2) * int(get_co2(data), 2))

