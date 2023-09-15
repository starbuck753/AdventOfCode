def parseinput(input):
  
  rows = input.splitlines()

  for r in rows:
    break  
  
  
  return


def solvepartone(input):

  result = 0

  #parseinput(input)
  up = input.count('(')
  down = len(input)-up #input.count(')')

  result = up - down

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = 0

  #parseinput(input)
  floor, pos = 0, 0

  for c in input:
    if c == '(':
      floor += 1  
    else:
      floor -= 1

    pos +=1
    if floor == -1:
      break


  result = pos

  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """)())())"""
sampleexpetedresultone = -3
sampleexpetedresulttwo = 0

file = open("day1.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


#assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)