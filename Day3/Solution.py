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


def Part2():
    with open("input.txt", "r") as file:
        banks = [line.strip() for line in file]

    res = 0
    for bank in banks:
        joltage = [0] * 12
        bank_len = len(bank)

        for i, digit_char in enumerate(bank):
            digit = int(digit_char)
            for j in range(12 - min(12, bank_len - i), 12):
                joltage_digit = joltage[j]
                if joltage_digit < digit:
                    joltage[j] = digit
                    for k in range(j+1, 12):
                        joltage[k] = 0
                    break

        joltage_val = 0
        for jolt in joltage:
            joltage_val = (joltage_val * 10) + jolt
        res += joltage_val

    print(res)


Part2()
