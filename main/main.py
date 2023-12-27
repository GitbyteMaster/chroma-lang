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
  while n != len(script)-1:
    n += 1
    if script[n] != "":
      parsed = lexer.parse(script[n])

      # Check parsed line
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
              lasterr.append("2")
              lasterr.append(n)
              parent = True
            elif lasterr[1] != n:
              lasterr[0] = "2"
              lasterr[1] = n
              parent = True
            error.SyntaxError(str(n+1), f"Operator \'{parsed[x]['contents']}\' missing \'int\' or \'float\'.", parent)
          else:
            contents = parsed[x]["operation"]["obj1"]
            try:
              parsed[x]["operation"]["obj1"]["type"]
            except TypeError:
              error.SyntaxError(str(n+1), f"Invalid syntax.", parent)
            else:
              if not parsed[x]["operation"]["obj1"]["type"] in ["int", "float", "operator"]:
                parent = False
                if lasterr == []:
                  lasterr.append("2")
                  lasterr.append(n)
                  parent = True
                elif lasterr[1] != n:
                  lasterr[0] = "2"
                  lasterr[1] = n
                  parent = True
                error.SyntaxError(str(n+1), f"Expected \'int\' or \'float\', not \'{parsed[x]['operation']['obj1']['type']}\'.", parent)
