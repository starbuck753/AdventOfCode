def solvepartone(input):

  result = 0

  rows = input.splitlines()
  
  for r in rows:
    pairs = r.split(',')
    section1 = pairs[0].split('-')
    section2 = pairs[1].split('-')

    if (int(section1[0]) >= int(section2[0]) and int(section1[1]) <= int(section2[1])) or (int(section2[0]) >= int(section1[0]) and int(section2[1]) <= int(section1[1])):
      result = result + 1


  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = 0

  rows = input.splitlines()
  
  for r in rows:
    pairs = r.split(',')
    section1 = pairs[0].split('-')
    section2 = pairs[1].split('-')

    if (int(section1[0]) >= int(section2[0]) and int(section1[0]) <= int(section2[1])) or (int(section2[0]) >= int(section1[0]) and int(section2[0]) <= int(section1[1])):
      result = result + 1


  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
sampleexpetedresultone = 2
sampleexpetedresulttwo = 4

file = open("day04.txt", "r")
input = file.read()

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)

print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)

print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)