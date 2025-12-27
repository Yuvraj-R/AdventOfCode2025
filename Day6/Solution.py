from math import prod


def Part1():
    with open("input.txt", "r") as file:
        rows = [line.split() for line in file]

    ops = rows[-1]
    nums_rows = [list(map(int, row)) for row in rows[:-1]]

    op_fn = {'+': sum, '*': prod}

    res = 0
    for col, op in zip(zip(*nums_rows), ops):
        res += op_fn[op](col)

    print(res)


Part1()
