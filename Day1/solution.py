def Part1():
    dial, password = 50, 0

    with open("rotations.txt", "r") as file:
        for line in file:
            direction, rotation = line[0], int(line[1:])
            if direction == 'L':
                rotation = -rotation

            dial = (dial + rotation) % 100

            if dial == 0:
                password += 1

    print(password)


Part1()

# --- PART 2 --- #


def Part2():
    dial, password = 50, 0

    with open("rotations.txt", "r") as file:
        for line in file:
            direction = line[0]
            rotation = int(line[1:])

            if direction == 'L':
                rotation = -rotation

            target = dial + rotation

            crossings = abs(target // 100 - dial // 100)
            password += crossings

            dial = target % 100

    print(password)


Part2()
