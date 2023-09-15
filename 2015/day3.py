
def solvepartone(input):

  result = 0
  pos, houses = "0,0", []
  houses.append(pos)
  
  for move in input:
    x, y = pos.split(',')
    x, y, = int(x), int(y)
    if move == '^':
      y -= 1
    elif move == 'v':
      y += 1
    elif move == '<':
      x -= 1
    elif move == '>':
      x += 1
    
    pos = str(x) + ',' + str(y)
    houses.append(pos)
  
  result = len(set(houses))

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = 0
  pos = {
    0 : "0,0",
    1 : "0,0"
  }
  santa, robo = [], []
  turno = 0
  santa.append(pos[turno%2])
  robo.append(pos[turno%2])

  for move in input:
    x, y = pos[turno%2].split(',')
    x, y, = int(x), int(y)
    if move == '^':
      y -= 1
    elif move == 'v':
      y += 1
    elif move == '<':
      x -= 1
    elif move == '>':
      x += 1
    
    pos[turno%2] = str(x) + ',' + str(y)
    
    if not turno%2:
      santa.append(pos[turno%2])
    else:
      robo.append(pos[turno%2])
    
    turno +=1
  
  allhuses = santa + robo
  result = len(set(allhuses))

  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """^v^v^v^v^v"""
sampleexpetedresultone = 2
sampleexpetedresulttwo = 11

file = open("day3.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)