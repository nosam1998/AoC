import string

t = 0

def slow_test(a, b, x, y):
    one = set(range(a, b+1))
    two = set(range(x, y+1))
    # print(f"One: {one}")
    # print(f"Two: {two}")
    overlap = one & two
    # print(f"Overlap between ({a}, {b}) and ({x}, {y}) is {len(overlap)} nums of: {overlap}")
    global t
    if len(overlap) > 0:
        t += 1


def is_inclusive(l):
    a, b, x, y = l[0][0], l[0][1], l[1][0], l[1][1]
    slow_test(a, b, x, y)
    if a <= x and b >= y:
        return True
    elif x <= a and y >= b:
        return True
    elif len(set({a, b, x, y})) < 4:
        return True
    return False

def main():
    answer = 0

    with open("input.txt", "r") as f:
        for i, line in enumerate(f):
            line = line.strip()
            pairs = [[int(i) for i in pair.split("-")] for pair in line.split(",")]
            if is_inclusive(pairs):
                answer += 1

    return answer

answer = main()
print(f"main() answer: {answer}")
print(f"Overlap slow test: {t}")
if answer == t:
    print("GOOD!")
else:
    print("Bad...")
