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
            direction, rotation = line[0], int(line[1:].strip())

            if direction == 'L':
                rotation = -rotation

            # Large rotations can cross 0 multiple times; count every crossing.
            if rotation > 0:
                distance_to_zero = 100 if dial % 100 == 0 else 100 - \
                    (dial % 100)
                clicks = 0 if rotation < distance_to_zero else 1 + \
                    (rotation - distance_to_zero) // 100
            elif rotation < 0:
                distance_to_zero = dial % 100 or 100
                steps = -rotation
                clicks = 0 if steps < distance_to_zero else 1 + \
                    (steps - distance_to_zero) // 100
            else:
                clicks = 0
            password += clicks

            new_dial = (dial + rotation) % 100

            dial = new_dial

    print(password)


Part2()
