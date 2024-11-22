import random
import numpy as np

def create_population():
    # Create population according to given proportions
    population = []
    population.extend([1] * 350000)    # 35% vote +1
    population.extend([-1] * 400000)   # 40% vote -1
    population.extend([0] * 250000)    # 25% vote 0
    random.shuffle(population)
    return population

def check_minus_one_majority(sample):
    # Count votes in sample
    counts = {-1: 0, 0: 0, 1: 0}
    for vote in sample:
        counts[vote] += 1
    # -1 has majority if it has more votes than both 0 and 1 combined
    return counts[-1] > counts[0] + counts[1]

def run_experiment(population, sample_size, num_trials=200):
    majority_minus_one_count = 0
    
    for _ in range(num_trials):
        # Take random sample
        sample = random.sample(population, sample_size)
        if check_minus_one_majority(sample):
            majority_minus_one_count += 1
            
    return majority_minus_one_count / num_trials

# Create population
population = create_population()

# Test different sample sizes
sample_sizes = [1, 2, 3, 4, 5, 10, 120, 250]
for size in sample_sizes:
    prob = run_experiment(population, size)
    print(f"Sample size {size}: Probability of -1 majority = {prob:.3f}")


# left, right = 0, 10
# target_prob = 0.9
# best_size = -1
# best_prob = 0

# while left <= right:
#     mid = (left + right) // 2
#     prob = run_experiment(population, mid)
#     print(f"Trying size {mid}, got probability {prob:.3f}")
    
#     if abs(prob - target_prob) < abs(best_prob - target_prob):
#         best_size = mid
#         best_prob = prob
    
#     if prob < target_prob:
#         left = mid + 1
#     else:
#         right = mid - 1

# print(f"\nFor probability ≈ 0.9, recommended sample size: {best_size}")
# print(f"Achieved probability: {best_prob:.3f}")