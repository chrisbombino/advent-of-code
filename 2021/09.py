from utils import *

data = read_aoc_data(9).splitlines()
caves = [[int(y) for y in x] for x in data]

# part 1
low_points = []
low_point_indices = []

def is_low_point(i, j):
    h = caves[i][j]

    above = below = left = right = float('inf')

    if i > 0: above = caves[i-1][j]
    if i < len(caves) - 1: below = caves[i+1][j]
    if j > 0: left = caves[i][j-1]
    if j < len(caves[0]) - 1: right = caves[i][j+1]

    return all([h < above, h < below, h < left, h < right])


for i, cave in enumerate(caves):
    for j, height in enumerate(cave):
        if is_low_point(i, j):
            low_points.append(height)
            low_point_indices.append((i,j)) # for part 2

risk_levels = map(lambda x: x+1, low_points)
print(f"Sum of risk levels: {sum(risk_levels)}")

# part 2
visited = [[False for y in x] for x in caves]
basin_sizes = []

def _dfs(i,j) -> int:
    if any([i < 0, i >= len(caves), j < 0, j >= len(caves[0])]):
        return 0
    
    if visited[i][j] or caves[i][j] == 9:
        return 0
    
    visited[i][j] = True
    return 1 + _dfs(i-1,j) + _dfs(i+1,j) + _dfs(i,j-1) + _dfs(i,j+1)

def basin_size_dfs(i,j) -> int:
    return _dfs(i,j)

for i,j in low_point_indices:
    basin_sizes.append(basin_size_dfs(i,j))

basin_sizes.sort(reverse=True)

print(f"Part 2: { basin_sizes[0] * basin_sizes[1] * basin_sizes[2] }")

