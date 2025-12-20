def Part1():
    with open("input.txt", "r") as file:
        banks = [line.strip() for line in file]

    res = 0
    for bank in banks:
        max_joltage, highest_val = 0, 0

        for digit_char in bank:
            digit = int(digit_char)

            joltage = highest_val * 10 + int(digit)

            if joltage > max_joltage:
                max_joltage = joltage

            if digit > highest_val:
                highest_val = digit

        res += max_joltage

    print(res)


Part1()
