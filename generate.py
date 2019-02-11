import json
import random

with open('patterns.json') as patterns_file:
    patterns = json.load(patterns_file)

with open('sources.json') as sources_file:
    sources = json.load(sources_file)

with open('results.json') as results_file:
    results = json.load(results_file)

pattern, flipped = random.choice(patterns)

pattern = pattern.replace('\\', '')

if flipped:
    print(pattern.format(random.choice(results), random.choice(sources)))

else:
    print(pattern.format(random.choice(sources), random.choice(results)))
