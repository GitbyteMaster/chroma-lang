import mathstack
import error


def tokenize(string):
  n = -1
  tokens = [""]
  while not n == len(string)-1:
    n += 1
    if not string[n] in ["  ", " "]:
      if string[n] == "\"":
        n += 1
        tokens.append("")
        while not string[n] == "\"":
          tokens[len(tokens)-1] = f"{tokens[len(tokens)-1]}{string[n]}"
          n += 1
        tokens[len(tokens)-1] = f"\"{tokens[len(tokens)-1]}\""
      else:
        tokens[len(tokens)-1] = f"{tokens[len(tokens)-1]}{string[n]}"
    else:
      tokens.append("")
  return tokens
'''
Unfinished parser. Putting this here for now, just in case whatever happens. File was almost lost anyway.
'''
def parse(tokens):
  nodes = {}
  for x in tokenize(tokens):
    token = x
    if len(token) != 0:
      if f"{token[0]}{token[len(token)-1]}" == "\"\"":
        nodes[f"param{len(nodes)+1}"] = {"type":"str", "contents":token.split("\"")[1], "len":len(token)-2}
      else:
        try:
          int(token)
        except TypeError:
          try:
            float(token)
          except TypeError:
            if token in ["true", "True", "false", "False"]:
              nodes[f"param{len(nodes)+1}"] = {"type":"boolean", "contents":token.split("\"")[1]}
            else:
              nodes[f"param{len(nodes)+1}"] = "error1"
          else:
            nodes[f"param{len(nodes)+1}"] = {"type":"float", "contents":token, "len":len(token)-2}
        except ValueError:
          nodes[f"param{len(nodes)+1}"] = "error1"
        else:
          nodes[f"param{len(nodes)+1}"] = {"type":"int", "contents":token, "len":len(token)-2}
  return nodes