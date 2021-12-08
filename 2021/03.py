from utils import *

data = read_aoc_data(3).splitlines()
num_bits = len(data[0])

def binary_to_int(binary_num: str) -> int:
    decimal_num = 0
    tens = 1

    for bit in binary_num[::-1]:
        decimal_num += tens * int(bit)
        tens *= 2

    return decimal_num

#part 1
gamma = ""
epsilon = ""

for bit_pos in range(num_bits):
    num_ones = 0
    for binary_num in data:
        bit = binary_num[bit_pos]
        
        if int(bit) == 1:
            num_ones += 1
    
    # find the most/least common bit for this position
    if num_ones >= len(data) / 2: # 1 is most common
        gamma += "1"
        epsilon += "0"
    else: # 0 is most common
        gamma += "0"
        epsilon += "1"

power_consumption = binary_to_int(gamma) * binary_to_int(epsilon)
print(f"Power Consumption: {power_consumption}")

# part 2
o2_possibilities = data
co2_possibilities = data

for bit_pos in range(num_bits):
    num_ones = 0
    for binary_num in o2_possibilities:
        bit = binary_num[bit_pos]
        
        if bit == "1":
            num_ones += 1

    if len(o2_possibilities) == 1:
        break
    b = "1" if num_ones >= len(o2_possibilities) / 2 else "0"
    o2_possibilities = [x for x in o2_possibilities if x[bit_pos] == b]

    
for bit_pos in range(num_bits):
    num_ones = 0
    for binary_num in co2_possibilities:
        bit = binary_num[bit_pos]
        
        if bit == "1":
            num_ones += 1
    
    if len(co2_possibilities) == 1:
        break
    b = "1" if num_ones < len(co2_possibilities) / 2 else "0"
    co2_possibilities = [x for x in co2_possibilities if x[bit_pos] == b]
        

o2_gen_rating = o2_possibilities[0]
co2_scrub_rating = co2_possibilities[0]

life_support_rating = binary_to_int(o2_gen_rating) * binary_to_int(co2_scrub_rating)
print(f"Life Support Rating: {life_support_rating}")

