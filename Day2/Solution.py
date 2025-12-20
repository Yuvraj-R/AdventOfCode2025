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
