import mathstack

def tokenize(string):
    n = -1
    tokens = []
    param = []
    while not n == len(string)-1:
        n += 1
        if not string[n] in "    ":
            if string[n] == "\"":
                tokens.append("")
                param.append("str")
                n += 1
                while not string[n] == "\"":
                    tokens[len(tokens)-1] = f"{tokens[len(tokens)-1]}{string[n]}"
                    n += 1
            if string[n] in "0987654321":
                tokens.append("")
                param.append("num")
                while string[n] in "0987654321+-/*":
                    tokens[len(tokens)-1] = f"{tokens[len(tokens)-1]}{string[n]}"
                    n += 1
                tokens[len(tokens)-1] = mathstack.pemdas(f";{tokens[len(tokens)-1]};")
    return tokens
print(tokenize("\"hihi\"0+9 "))
