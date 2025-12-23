def Part1():
    with open("input.txt", "r") as file:
        grid = [line.strip() for line in file]

    R, C = len(grid), len(grid[0])
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]

    res = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] != '@':
                continue

            adj = 0
            for dr, dc in dirs:
                rr, cc = r + dr, c + dc
                if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == '@':
                    adj += 1
                    if adj == 4:
                        break

            if adj < 4:
                res += 1

    print(res)


Part1()

# --- PART 2 --- #


def processGrid(grid):
    R, C = len(grid), len(grid[0])
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]

    to_remove = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] != '@':
                continue

            adj = 0
            for dr, dc in dirs:
                rr, cc = r + dr, c + dc
                if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == '@':
                    adj += 1
                    if adj == 4:
                        break

            if adj < 4:
                to_remove.append((r, c))

    for r, c in to_remove:
        grid[r][c] = 'x'

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'x':
                grid[r][c] = '.'

    return len(to_remove)


def Part2():
    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]

    total = 0
    while True:
        removed = processGrid(grid)
        if removed == 0:
            break
        total += removed

    print(total)


Part2()
