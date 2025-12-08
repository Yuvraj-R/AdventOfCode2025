with open("rotations.txt", "r") as file:
    rotations = [(l[0], int(l[1:])) for l in file.read().split()]

dial, password = 50, 0
for dr, rot in rotations:
    if dr == 'L':
        rot *= -1
    dial = (dial + rot) % 100
    if dial == 0:
        password += 1


print(password)
