from re import search

def isnice(input : str):

  # 1. Contains at least 3 vowels
  if input.count('a') + input.count('e') + input.count('i') + input.count('o') + input.count('u') < 3:
    return False
  
  # 2. Contains a letter twice in a row
  p, two = '', False
  for c in input:
    if c == p:
      two = True
      break
    p = c

  if not two : return False

  # 3. Does NOT contain the strings ab, cd, pq, xy
  if search("ab|cd|pq|xy", input) != None:
    return False

  return True


def isreallynice(input : str):
  
  # 1. It contains a pair of any two letters that appears at least twice in the string without overlapping
  #   eg. xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
  one = False
  for i in range(len(input)-1):
    letters = input[i:i+2]
    if input[i+2:].find(letters) != -1:
      one = True
      break

  if not one : return False  
  
  # 2. It contains at least one letter which repeats with exactly one letter between them
  #   eg. xyx, abcdefeghi (efe), or even aaa.
  two = False
  for i in range(len(input)-2):
    if input[i] == input[i+2]:
      two = True
      break

  if not two : return False    

  return True

def solvepartone(input : str):

  result = 0
  
  for word in input.splitlines():
    if isnice(word) : result += 1

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input : str):

  result = 0
  
  for word in input.splitlines():
    if isreallynice(word) : result += 1


  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb"""
sampleexpetedresultone = 2
sampleexpetedresulttwo = 0

file = open("day5.txt", "r")
input = file.read()

assert isnice("aaa") == True
assert isnice("jchzalrnumimnmhp") == False
assert isnice("haegwjzuvuyypxyu") == False
assert isnice("dvszwmarrgswjxmb") == False

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


#assert solveparttwo(sampleinput) == sampleexpetedresulttwo

assert isreallynice("qjhvhtzxzqqjkmpb") == True
assert isreallynice("paaatposa") == False
assert isreallynice("ieodomkazucvgmuy") == False

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)