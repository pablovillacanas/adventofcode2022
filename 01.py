from functools import reduce
import numpy as np

with open('input01.txt', 'r') as f:
    data = f.read()
    elves = data.split('\n\n')
    calories = []
    for elf in elves:
        snacks = elf.split('\n')
        calories.append(reduce(lambda acc, curr: int(acc) +
                        int(curr), map(lambda x: int(x), snacks)))
    calories.sort()
    top3carriers = calories[len(calories)-3: len(calories)]
    print(top3carriers)
    sumtotal3carriers = reduce(lambda acc, curr: acc + curr, top3carriers)
    print(sumtotal3carriers)
