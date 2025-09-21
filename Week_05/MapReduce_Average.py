#!/usr/bin/python

import string

dataset = """
John,80
John,40
Jane,97
Jane,81
Alice,60
Alice,78
Alice,88
Bob,64
Bob,83
James,74
James,68
Michael,72
Robert,68
Maria,66
"""

def map_function(text):
    part = text.split(",")
    yield (part[0], part[1], 1)

def reduce_function(pairs):
    result = {}
    for name, score, count in pairs:
        if name in result:
            result[name][0] += int(score)
            result[name][1] += count
        else:
            result[name] = [int(score), count]
    return result

person_map = []

# Sanitize the dataset
dataset = dataset.strip()

for line in dataset.splitlines():
    person_map.extend(map_function(line))

print("Mapped Data:")
print(person_map)

print("\nReduced Data:")
for name, [score, count] in reduce_function(person_map).items():
    print(f"{name}: {score / count}")