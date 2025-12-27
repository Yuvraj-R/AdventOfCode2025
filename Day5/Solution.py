import bisect

### HELPERS ###


def mergeIntervals(intervals):
    intervals.sort()

    res = []
    for start, end in intervals:
        if res and start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])
    return res

### PART 1 ###


def Part1():
    with open("input.txt", "r") as file:
        id_ranges, ids = file.read().split("\n\n")

    id_ranges = [tuple(map(int, line.split('-')))
                 for line in id_ranges.split()]
    ids = [int(x) for x in ids.split()]

    merged_id_ranges = mergeIntervals(id_ranges)

    starts = [r[0] for r in merged_id_ranges]

    count = 0
    for x in ids:
        i = bisect.bisect_right(starts, x) - 1
        if i >= 0 and x <= merged_id_ranges[i][1]:
            count += 1

    print(count)


Part1()

### PART 2 ###


def Part2():
    with open("input.txt", "r") as file:
        id_ranges, ids = file.read().split("\n\n")

    id_ranges = [tuple(map(int, line.split('-')))
                 for line in id_ranges.split()]
    ids = [int(x) for x in ids.split()]

    merged_id_ranges = mergeIntervals(id_ranges)

    res = sum(end - start + 1 for start, end in merged_id_ranges)
    print(res)


Part2()
