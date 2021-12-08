from utils import *

data_str = read_aoc_data(1)
data = list(map(int, data_str.splitlines()))

# part 1
num_depth_increases = 0
prev = float('inf')

for depth in data:
    if depth > prev:
        num_depth_increases += 1
    prev = depth

print(f"Number of depth increases: {num_depth_increases}")

#part 2
num_increases_sliding_window = 0
prev = float('inf')

window_size = 3

for i, _ in enumerate(data[2:]):
    three_measurement_window_depth = sum(data[i:i+window_size])

    if three_measurement_window_depth > prev:
        num_increases_sliding_window += 1
    prev = three_measurement_window_depth

print(f"Number of depth increases (sliding window): {num_increases_sliding_window}")
