def Part1():
    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]

    def countAdjRolls(r, c):
        adjacent_positions = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                              (r, c - 1), (r, c + 1), (r + 1, c - 1),
                              (r + 1, c), (r + 1, c + 1)]
        return sum(isRoll(adj_r, adj_c) for adj_r, adj_c in adjacent_positions)

    def isRoll(r, c):
        nonlocal grid
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '@'

    res = 0
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if grid[r][c] == '@' and countAdjRolls(r, c) < 4:
                res += 1

    print(res)


Part1()
