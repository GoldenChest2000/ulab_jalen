import numpy as np

def roll_dice(n):
    """
    Rolls a random number from 1-6 and adds it to a list for usage in computing total scores
    """
    return np.random.randint(1, 7, size=n).tolist()

n = 10
dice_rolls = roll_dice(n)
print(f"{n} dice rolls: {dice_rolls}")