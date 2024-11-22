import numpy as np

def simulate_walk(t):
    position = 0
    crossings = 0
    prev_position = 0
    
    for _ in range(t):
        position += np.random.choice([-1, 1])
        if (prev_position > 0 and position <= 0) or (prev_position < 0 and position >= 0):
            crossings += 1
        prev_position = position
    
    return crossings

# Run experiments for different values of t
t_values = [40000, 90000, 160000]
np.random.seed(42)  # For reproducibility

for t in t_values:
    total_crossings = sum(simulate_walk(t) for _ in range(50))
    avg_crossings = total_crossings / 50
    print(f"t={t}: Average crossings = {avg_crossings:.2f}")
