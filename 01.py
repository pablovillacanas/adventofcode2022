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
    sumtotal3carriers = reduce(lambda acc, curr: acc + curr, top3carriers)
    # Answer to Q1 (elf with most calories) && Q2 (three most elves carrying)
    print(sumtotal3carriers)
