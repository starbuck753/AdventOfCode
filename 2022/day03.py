def solvepartone(input):

  result = 0
  array = ""

  rows = input.splitlines()
  
  for r in rows:
    half = int(len(r)/2)
    comp1 = r[:half]
    comp2 = r[half:]

    for c in comp1:
      if comp2.find(c) != -1:
        array = array + c
        break

  

  for c in array:
    if c == c.lower(): #Es minuscula
      #print(c, ord(c), ord('a')+1, ord(c) - ord('a') + 1)
      result = result + ord(c) - ord('a') + 1
    else:
      #print(c, ord(c), ord('a')+28, ord(c) - ord('A') + 27)
      result = result + ord(c) - ord('A') + 27
      
    
  #print(result)

  return result


def solveparttwo(input):

  result = 0
  array = ""

  rows = input.splitlines()
  
  for i in range(0, len(rows), 3):
    
    first = rows[i]
    second = rows[i+1]
    third = rows[i+2]

    for c in first:
      if second.find(c) != -1:
        if third.find(c) != -1:
          array = array + c
          break    
  

  for c in array:
    if c == c.lower(): #Es minuscula
      #print(c, ord(c), ord('a')+1, ord(c) - ord('a') + 1)
      result = result + ord(c) - ord('a') + 1
    else:
      #print(c, ord(c), ord('a')+28, ord(c) - ord('A') + 27)
      result = result + ord(c) - ord('A') + 27
      
    
  #print(result)

  return result



# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
sampleexpetedresultone = 157
sampleexpetedresulttwo = 70

file = open("day03.txt", "r")
input = file.read()

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)

print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)

print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)