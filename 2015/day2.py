def parseinput(input):
  
  rows = input.splitlines()
  presents = []
  
  for r in rows:
    l, w, h = r.split('x')
    present = [int(l), int(w), int(h)]
    present.sort()
    presents.append(present)
  
  return presents


def solvepartone(input):

  result = 0

  presents = parseinput(input)
  
  for present in presents:
    l, w, h = present
    result += (3*l*w) + (2*w*h) + (2*h*l) #+ min(l*w,w*h,h*l)
  
  #print (result)

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = 0

  presents = parseinput(input)

  for present in presents:
    l, w, h = present
    result += 2*l+2*w + (l*w*h) #min(2*l+2*w, 2*w+2*h, 2*h+2*l) + (l*w*h)
  
  #print (result)

  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """2x3x4"""
sampleexpetedresultone = 58
sampleexpetedresulttwo = 34

file = open("day2.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)