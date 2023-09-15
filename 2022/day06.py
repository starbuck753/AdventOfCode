def getPosition(input, cont):

  array = []

  for i in range(0, len(input)-cont):
    #print(array, len(array), set(array))
    if len(set(input[i:i+cont])) == cont:
      return i+cont


def solvepartone(input):

  return getPosition(input, 4)

# ----------------------------------------------------------------------------

def solveparttwo(input):

  return getPosition(input, 14)
  


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
sampleexpetedresultone = 10
sampleexpetedresulttwo = 29

file = open("day06.txt", "r")
input = file.read()

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)

print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)

print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)