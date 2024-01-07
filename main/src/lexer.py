import src.tokens as tk

digits = "0123456789"
escape = ["\t", "\n", "\v", "\f", "\r"]
whitespace = ["  ", " "]

err = []

def tokenize(text):
  tokens = []
  n = -1
  chunk = ""
  while n != len(text)-1:
    n += 1
    chunk = f"{chunk}{text[n]}"
    if text[n] in digits+".":
      if text[n+1] not in digits+".":
        try: int(chunk)
        except ValueError:
          try: float(chunk)
          except ValueError:
            err.append([1, chunk])
            chunk = ""
          else:
            tokens.append([tk.FLOAT, float(chunk)])
            chunk = ""
        else:
          tokens.append([tk.INT, int(chunk)])
          chunk = ""
      else:
        pass
    elif chunk in whitespace:
      tokens.append([tk.WHITESPACE, chunk])
      chunk = ""
    elif text[n] == "\"" and chunk[0] == text[n] and len(chunk) > 1:
      tokens.append([tk.STR, chunk[1:len(chunk)-1]])
      chunk = ""
    elif text[n] in ["+", "-", "*", "/", "="]:
      if text[n-1] in ["=", "!"] and text[n] == "=":
        tokens[len(tokens)-1] = [tk.BOOL, f"{text[n-1]}{text[n]}"]
        chunk = ""
      else:
        tokens.append([tk.OPER, text[n]])
        chunk = ""
    
  return tokens