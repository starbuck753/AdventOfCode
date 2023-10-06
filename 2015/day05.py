from re import search, finditer, findall

def isnice(input : str):

  # 1. Contains at least 3 vowels
  if search(r'(.*[aeiou].*){3,}', input) == None:
    return False
  
  # 2. Contains a letter twice in a row
  if search(r'(\w)\1', input) == None:
    return False

  # 3. Does NOT contain the strings ab, cd, pq, xy
  if search(r'ab|cd|pq|xy', input) != None:
    return False

  return True


def isreallynice(input : str):
  
  # 1. It contains a pair of any two letters that appears at least twice in the string without overlapping
  #   eg. xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
  if search(r'(..).*\1', input) == None:
    return False
  
  # 2. It contains at least one letter which repeats with exactly one letter between them
  #   eg. xyx, abcdefeghi (efe), or even aaa.
  if search(r'(.).\1', input) == None:
    return False

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

file = open("day05.txt", "r")
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