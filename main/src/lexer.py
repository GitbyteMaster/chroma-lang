import mathstack
import error


def tokenize(string):
  n = -1
  tokens = [""]
  while n != len(string)-1:
    n += 1
    if not string[n] in ["  ", " ", "+", "-", "*", "/"]:
      if string[n] == "\"":
        n += 1
        tokens.append("")
        while string[n] != "\"":
          tokens[len(tokens)-1] = f"{tokens[len(tokens)-1]}{string[n]}"
          n += 1
        tokens[len(tokens)-1] = f"\"{tokens[len(tokens)-1]}\""
      else:
        tokens[len(tokens)-1] = f"{tokens[len(tokens)-1]}{string[n]}"
    elif string[n] in ["+", "-", "*", "/"]:
      tokens.append(string[n])
      tokens.append("")
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
        nodes[f"obj{len(nodes)+1}"] = {"type":"str", "contents":token.split("\"")[1], "len":len(token)-2}
      else:
        try:
          int(token)
        except TypeError:
          try:
            float(token)
          except TypeError:
            if token in ["true", "True", "false", "False", "null", "Null"]:
              nodes[f"obj{len(nodes)+1}"] = {"type":"boolean", "contents":token.split("\"")[1]}
            elif token in ["+", "-", "*", "/"]:
              nodes[f"obj{len(nodes)+1}"] = {"type":"operator", "contents":token}
            else:
              nodes[f"obj{len(nodes)+1}"] = "error1"
          else:
            nodes[f"obj{len(nodes)+1}"] = {"type":"float", "contents":token, "len":len(token)}
        except ValueError:
          if token in ["+", "-", "*", "/"]:
            nodes[f"obj{len(nodes)+1}"] = {"type":"operator", "contents":token}
          else:
            nodes[f"obj{len(nodes)+1}"] = "error1"
        else:
          nodes[f"obj{len(nodes)+1}"] = {"type":"int", "contents":token, "len":len(token)}
          

        if not "error" in nodes[f"obj{len(nodes)}"]:
          if nodes[f"obj{len(nodes)}"]["type"] in ["int", "float"]:
            if len(nodes) > 2:
              if nodes[f"obj{len(nodes)-1}"]["type"] == "operator":
                n = 0
                c = len(nodes)-3
                newnodes = {}
                while n != c:
                  n += 1
                  newnodes[f"obj{n}"] = nodes[f"obj{n}"]
                newnodes[f"obj{len(newnodes)+1}"] = {"type":"operator", "contents":nodes[f"obj{len(nodes)-1}"]["contents"],  "operation":{"obj1":nodes[f"obj{len(nodes)-2}"], "obj2":nodes[f"obj{len(nodes)}"]}}
                n += 2
                while n != len(nodes)-1:
                  n += 1
                  newnodes[f"obj{n-3}"] = nodes[f"obj{n}"]
                nodes = newnodes
  return nodes