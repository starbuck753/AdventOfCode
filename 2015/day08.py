
def solvepartone(input : str):

  result = 0

  digitallist = input.splitlines()
  
  total, string = 0, 0
  for line in digitallist:
    #print(line, len(line))
    total += len(line)

    slash = line.find('\\')
    newline = line
    #print(slash, newline)
    while slash != -1:

      if newline[slash+1] == '"':
        newline = newline[:slash] + '"' + newline[slash+2:]
      elif newline[slash+1] == '\\':
        newline = newline[:slash] + '&' + newline[slash+2:]
      elif newline[slash+1] == 'x':
        #print("Newline", newline[:slash], bytearray.fromhex(newline[slash+2:slash+4]).decode(), newline[slash+4:])
        #newline = newline[:slash] + chr(int(newline[slash+2:slash+4],16)) + newline[slash+4:]
        newline = newline[:slash] + '#' + newline[slash+4:]
      
      slash = newline.find('\\')

    print(line, newline[1:-1])
    string += len(newline[1:-1])
    #print(line, len(line), newline, len(newline[1:-1]))
  
  print(total, string)
  
  result = total - string

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input : str):

  result = 0

  digitallist = input.splitlines()

  total, string = 0, 0
  for line in digitallist:
    #print(line, len(line))
    total += len(line)

    newline = '"|' + line + '|"'
    slash = newline.find('\\')
    #print(slash, newline)
    while slash != -1:

      if newline[slash+1] == '"' or newline[slash+1] == '\\':
        newline = newline[:slash] + '||||' + newline[slash+2:]
      elif newline[slash+1] == 'x':
        newline = newline[:slash] + '||' + newline[slash+1:]
      
      slash = newline.find('\\')

    #print(line, newline)
    string += len(newline)
    #print(line, len(line), newline, len(newline))
  
  print(string - total)
  
  result = string - total

  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
file = open("day08eg.txt", "r")
sampleinput = file.read()

sampleexpetedresultone = 12
sampleexpetedresulttwo = 19


file = open("day08.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)