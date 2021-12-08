from utils import *

lines = read_aoc_data(2).splitlines()

commands = []

for line in lines:
    line = line.split(" ")
    commands.append((line[0], int(line[1])))

horizontal_position = 0
depth = 0

for command, distance in commands:
    if command == "forward":
        horizontal_position += distance
    elif command == "down":
        depth += distance
    else: # must be up
        depth -= distance


print(horizontal_position * depth)

commands = []

for line in lines:
    line = line.split(" ")
    commands.append((line[0], int(line[1])))

horizontal_position = 0
aim = 0
depth = 0

for command, distance in commands:
    if command == "forward":
        horizontal_position += distance
        depth += distance * aim
    elif command == "down":
        aim += distance
    else:
        aim -= distance


print(horizontal_position * depth)