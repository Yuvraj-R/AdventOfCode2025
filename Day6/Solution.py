from math import prod


def Part1():
    with open("input.txt", "r") as file:
        lines = [line.strip().split() for line in file]

    for i in range(len(lines) - 1):
        lines[i] = [int(n) for n in lines[i]]

    res = 0
    for i, op in enumerate(lines[-1]):
        nums = [line[i] for line in lines[:-1]]
        if op == '+':
            res += sum(nums)
        else:
            res += prod(nums)
    print(res)


Part1()
