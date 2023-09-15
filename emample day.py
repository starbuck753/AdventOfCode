def parseinput(input : str):
  
  rows = input.splitlines()

  for r in rows:
    break  
  
  
  return


def solvepartone(input : str):

  result = 0

  parseinput(input)


  return result

# ----------------------------------------------------------------------------

def solveparttwo(input : str):

  result = 0

  parseinput(input)



  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """"""
sampleexpetedresultone = 0
sampleexpetedresulttwo = 0

file = open("file.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)