from utils import *

data = read_aoc_data(10).splitlines()

# part 1
def balanced_opening_brackets(s):
    stack = []

    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    for char in s:
        if char in bracket_pairs: # opening bracket
            stack.append(char)
        else: # closing bracket
            if char != bracket_pairs[stack.pop()]:
                return True, char
    
    return False, None

score_lookup = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

syntax_error_score = 0

for line in data:
    corrupted, char = balanced_opening_brackets(line)

    if corrupted:
        syntax_error_score += score_lookup[char]

print(f"Syntax Error Score: {syntax_error_score}")

# part 2
def balanced_brackets_part2(s):
    stack = []
    score = 0
    
    score_lookup = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    for char in s:
        if char in bracket_pairs: # opening bracket
            stack.append(char)
        else: # closing bracket
            if char != bracket_pairs[stack.pop()]:
                print('code should never get here')
    
    for bracket in stack[::-1]:
        # brack will be opening bracket, need to find corresponding
        # closing bracket along with it's score
        score *= 5
        score += score_lookup[bracket_pairs[bracket]]

    return score

scores = []

for line in data:
    corrupted, _ = balanced_opening_brackets(line)

    if not corrupted:
        scores.append(balanced_brackets_part2(line))

scores.sort()
middle_score = scores[len(scores)//2]

print(f'Middle Score: {middle_score}')