def Part1():
    with open("input.txt", "r") as file:
        text = file.read().strip().replace("\n", "")
        ranges = [tuple(map(int, r.split("-"))) for r in text.split(",") if r]

    res = 0
    for start, end in ranges:
        for val in range(start, end + 1):
            s = str(val)
            L = len(s)
            if L % 2 == 0 and s[: L // 2] == s[L // 2:]:
                res += val

    print(res)


Part1()

# --- PART 2 --- #


def Part2():
    with open("input.txt", "r") as file:
        text = file.read().strip().replace("\n", "")
        ranges = [tuple(map(int, r.split("-"))) for r in text.split(",") if r]

    res = 0
    for start, end in ranges:
        for val in range(start, end + 1):
            s = str(val)
            # repeated-at-least-twice iff s is a substring of (s+s)[1:-1]
            if s in (s + s)[1:-1]:
                res += val

    print(res)


Part2()
