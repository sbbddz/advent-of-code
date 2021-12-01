with open("day1.txt") as file:
    input = list(map(lambda x: int(x), filter(lambda x: x.isnumeric(), file.read().split("\n"))))

parsedInput = [input[n: n+3] for n in range(0, len(input))]
input = list(map(lambda x: sum(x), parsedInput))

numberBefore = 0 
count = 0
for i in range(len(input)):
    diff = input[i] - numberBefore
    if (diff > 0 and i != 0):
        count += 1
    numberBefore = input[i]

print(count)
