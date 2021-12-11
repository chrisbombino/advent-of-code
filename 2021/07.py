from utils import *

data = list(map(int, read_aoc_data(7).splitlines()[0].split(",")))

# part 1
fuel = float('inf')
curr_fuel = 0

for num1 in data:
    for num2 in data:
        curr_fuel += abs(num2 - num1)
    fuel = min(fuel, curr_fuel)
    curr_fuel = 0

print(f"Part 1 Minimum Fuel: {fuel}")

# part 2
fuel = float('inf')
curr_fuel = 0

def fuel_burned(distance):
    fuel = 0

    for num in range(distance):
        fuel += num + 1
    
    return fuel

for num1 in data:
    for num2 in data:
        curr_fuel += fuel_burned(abs(num2 - num1))
    fuel = min(fuel, curr_fuel)
    curr_fuel = 0


print(f"Part 2 Minimum Fuel: {fuel}")
