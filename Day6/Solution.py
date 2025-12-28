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


def Part2():
    with open("input.txt", "r") as file:
        rows = [line for line in file]

    ops = rows[-1].split()
    nums_rows = [row[:-1] for row in rows[:-1]]
    nums_rows_split = [row[:-1].split() for row in rows[:-1]]

    op_fn = {'+': sum, '*': prod}

    res = 0
    for i, op in enumerate(ops):
        length = max(len(line[i]) for line in nums_rows_split)
        nums = [line[:length] for line in nums_rows]
        for i in range(len(nums_rows)):
            nums_rows[i] = nums_rows[i][length + 1:]

        # verticalize nums
        vertical_nums = []
        for i in range(length - 1, -1, -1):
            vertical_nums.append(int("".join(num[i] for num in nums)))

        res += op_fn[op](vertical_nums)

    print(res)


Part2()
