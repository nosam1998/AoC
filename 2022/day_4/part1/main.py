import string

def is_inclusive(l):
    a, b, x, y = l[0][0], l[0][1], l[1][0], l[1][1]

    if a <= x and b >= y:
        return True
    elif x <= a and y >= b:
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
print(main())