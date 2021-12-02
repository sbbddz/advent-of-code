with open("day2.txt") as file:
    data = file.read().split("\n")

depth = 0
horizontal = 0
aim = 0
for x in range(len(data)):
    if data[x] != '':
        parsed = data[x].split(" ")
        number = int(parsed[1])
        case = parsed[0]
        if (case == 'up'): 
            aim -= number
        elif (case == 'down'): 
            aim += number
        elif (case == 'forward'): 
            horizontal += number
            depth += aim * number

print(depth * horizontal)
