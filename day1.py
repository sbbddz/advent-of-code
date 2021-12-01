with open("day1.txt") as file:
    input = list(map(lambda x: int(x), filter(lambda x: x.isnumeric(), file.read().split("\n"))))

"""
    Initially was using hashmaps for solving this. 
    Joined the advent of code subreddit and watching solutions by surface I notice that
    I had the exercise solved I just was complicating myself
"""
numberBefore = 0 
count = 0
for i in range(len(input)):
    diff = input[i] - numberBefore
    if (diff > 0 and i != 0):
        count += 1
    numberBefore = input[i]

print(count)
