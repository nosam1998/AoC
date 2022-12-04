import string

def main():
    # alpha = string.ascii_lowercase + string.ascii_uppercase
    alpha_dict = {letter: i+1 for i, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)}
    running_num = 0
    common = None

    with open("input.txt", "r") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i % 3 == 0:
                if i >= 3:
                    common = common.pop()
                    running_num += alpha_dict[common]
                    print(f"Common character on group #{i//3} is {common}")
                common = set(line)
            else:
                common = common & set(line)
    
    common = common.pop()
    running_num += alpha_dict[common]
    return running_num
print(main())