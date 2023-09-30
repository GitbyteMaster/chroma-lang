def stack(equ):
    n = 0
    num = ""
    stackable = True
    n = 0
    num = ""
    eq = equ
    '''
Before you ask, yes. I do know that there are other types, other than integers. I'm working out the kinks.
    '''
    while stackable:
        while eq[n] in "1234567890":
            num = f"{num}{eq[n]}"
            n += 1
        op = 0
        if eq[n] in ["+", "-"]:
            if eq[n] == "+":
                op = 1
                n += 1
                numm = ""
                while eq[n] in "1234567890":
                    numm = f"{numm}{eq[n]}"
                    n += 1
                ad = int(num)+int(numm)
                num = f"{ad}"
            if eq[n] == "-":
                op = 1
                n += 1
                numm = ""
                while eq[n] in "1234567890":
                    numm = f"{numm}{eq[n]}"
                    n += 1
                ad = int(num)-int(numm)
                num = f"{ad}"
        if eq[n] in ["*", "/"]:
            if eq[n] == "*":
                op = 1
                n += 1
                numm = ""
                while eq[n] in "1234567890":
                    numm = f"{numm}{eq[n]}"
                    n += 1
                ad = int(num)*int(numm)
                num = f"{ad}"
            if eq[n] == "/":
                op = 1
                n += 1
                numm = ""
                while eq[n] in "1234567890":
                    numm = f"{numm}{eq[n]}"
                    n += 1
                ad = int(int(num)/int(numm))
                num = f"{ad}"
            
        if eq[n] == ";":
            stackable = False
    return num
def pemdas(equ):
    done = 0
    eq = equ
    n = 0
    while "*" in eq:
        n = eq.index("*")+1
        while eq[n] in "0987654321":
            n += 1
        n -= 1
        e = ""
        while eq[n] in "0987654321":
            e = f"{eq[n]}{e}"
            n -= 1
        e = f"{eq[n]}{e}"
        n -= 1
        while eq[n] in "0987654321":
            e = f"{eq[n]}{e}"
            n -= 1

        f = ""
        n = 0
        while not n == eq.index(e):
            f = f"{f}{eq[n]}"
            n += 1
        n += len(e)
        f = f"{f}" + stack(f"{e};")
        while not n == len(eq)-1:
            f = f"{f}{eq[n]}"
            n += 1
        eq = f
    while "/" in eq:
        n = eq.index("/")+1
        while eq[n] in "0987654321":
            n += 1
        n -= 1
        e = ""
        while eq[n] in "0987654321":
            e = f"{eq[n]}{e}"
            n -= 1
        e = f"{eq[n]}{e}"
        n -= 1
        while eq[n] in "0987654321":
            e = f"{eq[n]}{e}"
            n -= 1

        f = ""
        n = 0
        while not n == eq.index(e):
            f = f"{f}{eq[n]}"
            n += 1
        n += len(e)
        f = f"{f}" + stack(f"{e};")
        while not n == len(eq)-1:
            f = f"{f}{eq[n]}"
            n += 1 
        eq = f
    return stack(eq.split(";")[1]+";")
