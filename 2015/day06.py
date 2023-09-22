def parseinput(input : str):
  
  rows = input.splitlines()
  instrctions = []

  for r in rows:
    r = r.replace("turn ", "")
    action, init, _, end = r.split()
    
    instrctions.append([action, init, end])
  
  return instrctions


def solvepartone(input : str):

  instrctions = parseinput(input)
  #print(instrctions)
  lights = {}

  for todo in instrctions:
    x1, y1 = todo[1].split(',')
    x2, y2 = todo[2].split(',')
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    for x in range(x1,x2+1):
      for y in range(y1,y2+1):
        if todo[0] == "on":
          lights[str(x) + ',' + str(y)] = True
        elif todo[0] == "off":
          lights[str(x) + ',' + str(y)] = False
        else:
          lights[str(x) + ',' + str(y)] = lights.get(str(x) + ',' + str(y), False) ^ True

  on = [x for x, val in lights.items() if val]

  return len(on)

# ----------------------------------------------------------------------------

def solveparttwo(input : str):

  instrctions = parseinput(input)
  #print(instrctions)
  lights = {}

  for todo in instrctions:
    x1, y1 = todo[1].split(',')
    x2, y2 = todo[2].split(',')
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    for x in range(x1,x2+1):
      for y in range(y1,y2+1):
        val = lights.get(str(x) + ',' + str(y), 0)
        if todo[0] == "on":
          val += 1
        elif todo[0] == "off":
          val -= 1
          if val < 0 : val = 0
        else:
          val += 2
        
        lights[str(x) + ',' + str(y)] = val

  result = sum(lights.values())

  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """"""
sampleexpetedresultone = 0
sampleexpetedresulttwo = 0

file = open("day06.txt", "r")
input = file.read()

#assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)