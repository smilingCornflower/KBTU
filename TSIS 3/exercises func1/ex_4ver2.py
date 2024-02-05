def perm(line):
    stack = [(list(line), 0)]

    while stack:
        current, step = stack.pop()

        if step == len(current):
            print("".join(current))
        else:
            for i in range(step, len(current)):
                current[step], current[i] = current[i], current[step]
                stack.append((list(current), step + 1))
                current[step], current[i] = current[i], current[step]



line = "abc"
perm(line)