def Part1():
    with open("input.txt", "r") as file:
        ranges = [tuple(r.split("-")) for r in file.read().split(",")]

    res = 0
    for start, end in ranges:
        for val in range(int(start), int(end)+1):
            val_string = str(val)
            val_length = len(val_string)

            if val_length % 2 != 0:
                continue

            if val_string[:val_length//2] == val_string[val_length//2:]:
                res += val
    print(res)


Part1()

# --- PART 2 --- #


def Part2():
    with open("input.txt", "r") as file:
        ranges = [tuple(r.split("-")) for r in file.read().split(",")]

    res = 0
    for start, end in ranges:
        for val in range(int(start), int(end)+1):
            val_string = str(val)
            val_length = len(val_string)

            for i in range(1, (val_length // 2) + 1):
                if val_length % i != 0:
                    continue

                substrings = []
                p1, p2 = 0, i
                for k in range(val_length // i):
                    substrings.append(val_string[p1:p2])
                    p1, p2 = p2, p2 + i

                if all(s == substrings[0] for s in substrings):
                    res += val
                    break

    print(res)


Part2()
