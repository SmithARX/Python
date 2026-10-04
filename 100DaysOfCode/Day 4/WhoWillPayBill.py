import random
frinds = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st option
randomChoice = random.randint(0, 4)
print(frinds[randomChoice])

#2st option
print(random.choice(frinds))