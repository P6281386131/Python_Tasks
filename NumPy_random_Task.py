import numpy as np

# Simulate rolling two dice 1000 times
dice1 = np.random.randint(1, 7, size=1000)
dice2 = np.random.randint(1, 7, size=1000)

# Sum of both dice for each roll
sum_of_dice = dice1 + dice2

print("First 10 rolls of dice 1:", dice1[:10])
print("First 10 rolls of dice 2:", dice2[:10])
print("First 10 sums:", sum_of_dice[:10])
