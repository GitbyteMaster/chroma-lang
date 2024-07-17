import string

# Single character tokens

TOKENS = {
    "(":"LEFT_PAREN",
    ")":"RIGHT_PAREN",
    "|":"OR",
    "\"":"DOUBLE_QUOTATION",
    "\'":"QUOUTATION",
    "+":"PLUS",
    "-":"MINUS",
    "/":"FORWARD_SLASH",
    "\\":"BACKWARDS_SLASH",
    "*":"STAR",
    ".":"PERIOD",
    "[":"OPEN_BRACKET",
    "]":"CLOSED_BRACKET",
    ":":"COLON",
    "?":"QUESTION",
    ">":"MORE_THAN",
    "<":"LESS_THAN",
    "!":"EXCLAMATION",
    "&":"AMPERSAND",
    "=":"EQUALS"
    }

LITERAL = {
    "letters":string.ascii_letters,
    "numbers":string.digits
    }

WHITESPACE = string.whitespace

# Multi-character tokens

KEYWORDS = {
    "with":"KEYWORD_WITH",
    "while":"KEYWORD_WHILE",
    "as":"KEYWORD_AS"
    }
    
class internal:
    class log:
        def char(char, first_pos):
            cdef = TOKENS[char]
            fp = first_pos
            return [[cdef, char], fp, fp]
        def literal(char, first_pos):
            fp = first_pos
            return [["literal", char], fp, fp]

# Lexer
def tokenize(line):
    # Register every single character
    scan = []
    pos = -1
    for x in line:
        pos += 1
        if not line[pos] in WHITESPACE:
            try: TOKENS[line[pos]]
            except KeyError:
                if line[pos] in LITERAL["letters"] or line[pos] in LITERAL["numbers"]: scan.append(internal.log.literal(line[pos], pos))
                else: scan.append([["error", line[pos]], pos, pos]) # Register unknown character for error
            else: scan.append(internal.log.char(line[pos], pos))
        else: scan.append([["whitespace", line[pos]], pos, pos])
    # Combine "literals" (lone digits and letters) & form strings.
    combo = []
    counter = -1
    while counter != len(scan)-1:
        counter += 1
        if scan[counter][0][0] == "literal":
            if len(combo) == 0: combo.append(scan[counter])
            elif combo[len(combo)-1][0][0] == "literal":
                combo[len(combo)-1][0][1] += scan[counter][0][1]
                combo[len(combo)-1][2] += 1
            else: combo.append(scan[counter])
        elif scan[counter][0][0] in ["QUOTATION", "DOUBLE_QUOTATION"]:
            subcounter = counter+1
            if not subcounter > len(scan)-1:
                while scan[counter][0][0] != scan[subcounter][0][0]: subcounter += 1
                combo.append([["string", line[scan[counter][2]+1:scan[subcounter][1]]], scan[counter][2], scan[subcounter][1]])
                counter = subcounter
            else: combo.append([["error1", scan[counter][0][1]], scan[counter][1], scan[counter][1]])
        else: combo.append(scan[counter])
    # Identify integers
    for x in combo:
        try: int(x[0][1])
        except: pass
        else:
            x[0][0] = "integer"
            x[0][1] = int(x[0][1])
    return combo

# Parser
def parse(tokens): # (tokens) is a list of tokens.
    
