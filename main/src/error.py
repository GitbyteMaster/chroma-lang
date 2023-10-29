def positionline(line, parent):
  pos = len(line)+1
  n = -1
  if parent:
    spaces = line+" "
  else:
    spaces = ""
    while not n == len(line):
      n += 1
      spaces = f"{spaces} "
  spaces = f"{spaces}|"
  return spaces

def SyntaxError(line, message, parent):
    print(f"{positionline(line, parent)} SyntaxError:  {message}")
def FatalError(line, message, parent):
    print(f"{positionline(line, parent)} FatalError:  {message}")
    exit()