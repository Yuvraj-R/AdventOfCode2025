def Solution():
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


Solution()
