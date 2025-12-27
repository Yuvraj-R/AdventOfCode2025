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

    fixed = []
    for start, end in merged_id_ranges:
        if fixed and start <= fixed[-1][1]:
            if end > fixed[-1][1]:
                fixed[-1][1] = end
        else:
            fixed.append([start, end])

    import bisect
    starts = [r[0] for r in fixed]

    count = 0
    for x in ids:
        i = bisect.bisect_right(starts, x) - 1
        if i >= 0 and x <= fixed[i][1]:
            count += 1

    print(count)


Part1()
