#!/usr/bin/python

from collections import defaultdict
import string

# Taken from https://en.wikipedia.org/wiki/Python_(programming_language)
dataset = """
Python is a high-level, general-purpose programming language.
Its design philosophy emphasizes code readability with the use of significant indentation.
Python is dynamically type-checked and garbage-collected.
It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming.
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language.
Python 3.0, released in 2008, was a major revision and not completely backward-compatible with earlier versions.
Recent versions, such as Python 3.12, have added capabilities and keywords for typing (and more; e.g. increasing speed); helping with (optional) static typing.
Currently only versions in the 3.x series are supported.
Python consistently ranks as one of the most popular programming languages, and it has gained widespread use in the machine learning community.
It is widely taught as an introductory programming language.
"""

def map_function(text):
    for word in text.split():
        yield (word, 1)

def reduce_function(pairs):
    result = defaultdict(int)
    for word, count in pairs:
        result[word] += count
    return result

# Sanitize the dataset
dataset = dataset.strip().lower().replace("-", " ").translate(str.maketrans("", "", string.punctuation))

word_map = []

for line in dataset.splitlines():
    word_map.extend(map_function(line))

print("Word Map:")
print(word_map)

print("\nReduced Data:")
for word, amount in reduce_function(word_map).items():
    print(f"{word}: {amount}")