import sys
sys.path.append("main/src")

import error
import lexer

file = ""
script = file.split(";")
if script == ['']:
  error.FatalError("None", "File is empty", True)
else:
  n = -1
  lasterr = []
  while not n == len(script)-1:
    n += 1
    if script[n] != "":
      parsed = lexer.parse(script[n])
      print(parsed)
      for x in parsed:
        if "error" in parsed[x]:
          parent = False
          if lasterr == []:
            lasterr.append(parsed[x].split("error")[1])
            lasterr.append(n)
            parent = True
          elif lasterr[1] != n:
            lasterr[0] = parsed[x].split("error")[1]
            lasterr[1] = n
            parent = True
          if lasterr[0] == "1":
            error.SyntaxError(str(n+1), f"Invalid syntax.", parent)
        elif parsed[x]["type"] == "operator":
          try:
            parsed[x]["operation"]
          except KeyError:
            parent = False
            if lasterr == []:
              lasterr.append("error2")
              lasterr.append(n)
              parent = True
            elif lasterr[1] != n:
              lasterr[0] = "error2"
              lasterr[1] = n
              parent = True
            error.SyntaxError(str(n+1), f"Operator \''{parsed[x]['contents']}\' missing \'int\' or \'float\'.", parent)