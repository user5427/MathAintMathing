import torch
from tqdm import tqdm
import math

# Configuration
m = 9
n = 6
k1 = 3
k2 = 4
total_samples = 10_000_000   # For testing, change to a smaller number first
batch_size = 100_000_00  # The number of samples per batch to avoid out-of-memory on GPU
num_processes = 1  # We will run everything on a single GPU, so this is 1

coin_values = torch.tensor([1]*m + [2]*n, device='cuda')

# Efficient experiment functions
def throwing_coinsE1():
    # Generate random permutations for a batch of samples
    perm = torch.randint(0, len(coin_values), (batch_size, len(coin_values)), device='cuda')  # Multiple permutations
    morning_coins = coin_values[perm[:, :k1]]  # First k1 coins for each batch
    afternoon_coins = coin_values[perm[:, k1:k1 + k2]]  # Next k2 coins for each batch
    
    sum1 = morning_coins.sum(dim=1).float()
    return sum1.mean().item(), 0

def throwing_coinsE2():
    perm = torch.randint(0, len(coin_values), (batch_size, len(coin_values)), device='cuda')  # Multiple permutations
    morning_coins = coin_values[perm[:, :k1]]  
    afternoon_coins = coin_values[perm[:, k1:k1 + k2]]  
    
    sum2 = afternoon_coins.sum(dim=1).float()
    return sum2.mean().item(), 0

def throw1Sqrt():
    # Sample without replacement
    perm = torch.randint(0, len(coin_values), (batch_size, len(coin_values)), device='cuda')  # Multiple permutations
    morning_coins = coin_values[perm[:k1]]  # First k1 coins for morning
    afternoon_coins = coin_values[perm[k1:k1+k2]]  # Next k2 coins for afternoon
    
    dist = morning_coins.sum().float()
    return (dist ** 2).mean().item(), 0

def throw2Sqrt():
    # Sample without replacement
    perm = torch.randint(0, len(coin_values), (batch_size, len(coin_values)), device='cuda')  # Multiple permutations
    morning_coins = coin_values[perm[:k1]]  # First k1 coins for morning
    afternoon_coins = coin_values[perm[k1:k1+k2]]  # Next k2 coins for afternoon
    
    dist = afternoon_coins.sum().float()
    return (dist ** 2).mean().item(), 0

def AverageE12():
    # Sample without replacement
    perm = torch.randint(0, len(coin_values), (batch_size, len(coin_values)), device='cuda')  # Multiple permutations
    morning_coins = coin_values[perm[:k1]]  # First k1 coins for morning
    afternoon_coins = coin_values[perm[k1:k1+k2]]  # Next k2 coins for afternoon
    
    sum1 = morning_coins.sum().float()
    sum2 = afternoon_coins.sum().float()
    return (sum1 * sum2).mean().item(), 0

# Parallel simulation function that runs an experiment and keeps progress
def run_experiment(func, repeat, position=0):
    count = (0, 0)
    
    # Set up the progress bar for multi-batch simulations
    iterations = int(math.ceil(repeat / batch_size))
    iterator = tqdm(range(iterations), position=position, desc=f"Proc {position} only", leave=False)
    
    for _ in iterator:
        # if i % 10000 == 0:  # Update the progress display every 100 iterations
            # print(f"Proc {position} progress: {i}/{iterations}", end='\r')
        res = func()
        count = (count[0] + res[0], count[1] + res[1])
    
    return count[0] / (iterations+count[1])

if __name__ == '__main__':
    repeat = 10_000_000  # Total number of samples (adjust as needed)


    # Run the experiment
    avr1 = run_experiment(throwing_coinsE1, repeat)
    avr2 = run_experiment(throwing_coinsE2, repeat)
    
    avr1sqrt = run_experiment(throw1Sqrt, repeat)
    avr2sqrt = run_experiment(throw2Sqrt, repeat)
    
    avg12 = run_experiment(AverageE12, repeat)
    
    mathDispersion1 = avr1sqrt - avr1 ** 2
    mathDispersion2 = avr2sqrt - avr2 ** 2
    
    import os
    os.system("clear")  # Clear the console for better readability

    # Print the result
    print(f"Average of first: {avr1}")
    print(f"Average of second: {avr2}")
    print(f"Average of first sqrt: {avr1sqrt}")
    print(f"Average of second sqrt: {avr2sqrt}")
    print(f"Dispersion of first math: {mathDispersion1}")
    print(f"Dispersion of second math: {mathDispersion2}")
    qxy = (avg12 - avr1 * avr2) / math.sqrt(mathDispersion1 * mathDispersion2)
    
    print(f"Correlation coefficient: {qxy}")
    