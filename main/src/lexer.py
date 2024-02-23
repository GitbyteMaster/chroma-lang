import src.tokens as tk

digits = "0123456789"
escape = ["\t", "\n", "\v", "\f", "\r"]
whitespace = ["  ", " "]

err = []

def Token(type, con):
  if type != tk.STR:
    return [type, con, [n-(len(str(con))-1), n]]
  else:
    return [type, con, [n-(len(str(con))+1), n]]

def tokenize(text):
  tokens = []
  global n
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
            tokens.append(Token(tk.FLOAT, float(chunk)))
            chunk = ""
        else:
          tokens.append(Token(tk.INT, int(chunk)))
          chunk = ""
    elif chunk in whitespace:
      # Whitespace
      tokens.append(Token(tk.WHITESPACE, chunk))
      chunk = ""
    elif text[n] == "\"" and chunk[0] == text[n] and len(chunk) > 1 and text[n-1] != "\\":
      # String
      tokens.append(Token(tk.STR, chunk[1:len(chunk)-1]))
      chunk = ""
    elif text[n] in ["+", "-", "*", "/", "="]:
      if text[n-1] in ["=", "!"] and text[n] == "=":
        # Operator
        tokens[len(tokens)-1] = Token(tk.OPER, f"{text[n-1]}{text[n]}")
        chunk = ""
      else:
        tokens.append(Token(tk.OPER, text[n]))
        chunk = ""
    elif chunk in ["null", "Null", "true", "True", "false", "False"]:
      tokens.append(Token(tk.BOOL, chunk))
      chunk = ""

  if err == []:
    return tokens
  else:
    return err