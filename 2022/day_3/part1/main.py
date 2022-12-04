import string

def main():
    # alpha = string.ascii_lowercase + string.ascii_uppercase
    alpha_dict = {letter: i+1 for i, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)}
    running_num = 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            len_line = len(line) // 2
            comp_1 = line[:len_line]
            comp_2 = line[len_line:]
            diff = set(comp_1) & set(comp_2)
            diff = diff.pop()
            running_num += alpha_dict[diff]
            
    return running_num
print(main())