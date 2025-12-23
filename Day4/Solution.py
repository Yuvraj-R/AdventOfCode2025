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
