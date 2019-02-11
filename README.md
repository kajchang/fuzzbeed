# Fuzzbeed

Objective: Generating convincing fake BuzzFeed quiz names. I mean, how hard can it be?

## Approach

1. Quiz names seem to conform to a few patterns, so use regex to extract the source (what the quiz asks you) and result (what the quiz tells you).

2. Mix and match sources, results, and patterns to generate new quiz names.
