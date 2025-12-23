def Part1():
    # Pick exactly 2 digits (i < j) to maximize 10*d[i] + d[j]
    res = 0
    with open("input.txt", "r") as file:
        for line in file:
            s = line.strip()
            if len(s) < 2:
                continue

            best = 0
            max_suffix = -1  # best digit seen to the right so far

            # scan right -> left: for each tens digit, best ones digit is max digit after it
            for ch in reversed(s):
                d = ord(ch) - 48  # faster than int(ch)
                if max_suffix != -1:
                    cand = d * 10 + max_suffix
                    if cand > best:
                        best = cand
                if d > max_suffix:
                    max_suffix = d

            res += best

    print(res)


Part1()


def Part2():
    # Pick exactly 12 digits to form the largest possible number (max subsequence of length 12)
    K = 12
    res = 0
    with open("input.txt", "r") as file:
        for line in file:
            s = line.strip()
            n = len(s)

            drop = n - K           # how many digits we are allowed to skip total
            stack = []             # chosen digits (monotone decreasing-ish)

            for ch in s:
                d = ord(ch) - 48
                while drop and stack and stack[-1] < d:
                    stack.pop()
                    drop -= 1

                if len(stack) < K:
                    stack.append(d)
                else:
                    # stack already has K digits; skipping this digit uses up one "drop"
                    drop -= 1

            joltage_val = 0
            for d in stack:        # stack length is exactly K
                joltage_val = joltage_val * 10 + d

            res += joltage_val

    print(res)


Part2()
