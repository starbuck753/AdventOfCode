from datetime import datetime
from operator import countOf

def parseinput(input):
  
  rows = input.splitlines()
  elfos = {}
  x, y, e = 0, 0, 0
  
  for r in rows:
    x = 0
    for c in range(r.count('#')):
      x = r[x:].find('#') + x
      elfos[e] = [x, y]
      e += 1
      #print(r[x:].find('#'), x, y, r[x:], r.count('#'))
      x += 1
  
    y += 1
  
  return elfos

def aroundpositions(elfoslist, pos):

  #Check on all 9 positions
  nw = elfoslist.count([pos[0]-1, pos[1]-1]) #NW - x-1, y-1
  n = elfoslist.count([pos[0], pos[1]-1])   #N - x, y-1
  ne = elfoslist.count([pos[0]+1, pos[1]-1]) #NE - x+1, y-1
  e = elfoslist.count([pos[0]+1, pos[1]])   #E - x+1, y
  se = elfoslist.count([pos[0]+1, pos[1]+1]) #SE - x+1, y+1
  s = elfoslist.count([pos[0], pos[1]+1])   #S - x, y+1
  sw = elfoslist.count([pos[0]-1, pos[1]+1]) #SW - x-1, y+1
  w = elfoslist.count([pos[0]-1, pos[1]])   #W - x-1, y

  around = [
    1 if nw + n + ne >= 1 else 0,
    1 if ne + e + se >= 1 else 0,
    1 if sw + s + se >= 1 else 0,
    1 if nw + w + sw >= 1 else 0
  ]

  return around

"""def northpositions(elfoslist, pos):

  count = 0
  #Check on all north positions
  count += elfoslist.count([pos[0]-1, pos[1]-1]) #NW - x-1, y-1
  count += elfoslist.count([pos[0], pos[1]-1])   #N - x, y-1
  count += elfoslist.count([pos[0]+1, pos[1]-1]) #NE - x+1, y-1

  return count

def southpositions(elfoslist, pos):

  count = 0
  #Check on all south positions
  count += elfoslist.count([pos[0]+1, pos[1]+1]) #SE - x+1, y+1
  count += elfoslist.count([pos[0], pos[1]+1])   #S - x, y+1
  count += elfoslist.count([pos[0]-1, pos[1]+1]) #SW - x-1, y+1

  return count

def westpositions(elfoslist, pos):

  count = 0
  #Check on all west positions
  count += elfoslist.count([pos[0]-1, pos[1]-1]) #NW - x-1, y-1
  count += elfoslist.count([pos[0]-1, pos[1]+1]) #SW - x-1, y+1
  count += elfoslist.count([pos[0]-1, pos[1]])   #W - x-1, y

  return count

def eastpositions(elfoslist, pos):

  count = 0
  #Check on all east positions
  count += elfoslist.count([pos[0]+1, pos[1]-1]) #NE - x+1, y-1
  count += elfoslist.count([pos[0]+1, pos[1]])   #E - x+1, y
  count += elfoslist.count([pos[0]+1, pos[1]+1]) #SE - x+1, y+1

  return count
"""

def checkdirection(d, around):

  match d:
    case 'N':
      return True if around[0] == 0 else False
    case 'E':
      return True if around[1] == 0 else False
    case 'S':
      return True if around[2] == 0 else False
    case 'W':
      return True if around[3] == 0 else False

def newposition(d, pos):

  match d:
    case 'N': #N - x, y-1
      return [pos[0], pos[1]-1]
    case 'S': #S - x, y+1
      return [pos[0], pos[1]+1]
    case 'W': #W - x-1, y
      return [pos[0]-1, pos[1]]
    case 'E': #E - x+1, y
      return [pos[0]+1, pos[1]]


def solvepartone(input):

  result = 0

  elfos, elfosnew = {}, {}
  elfos = parseinput(input)
  #print (elfos)

  directions = "NSWE"

  for n in range(10):
    elfoslist = list(elfos.values()) 
    for elfo, pos in elfos.items():
      #Check all positions around the elfo
      aroundelfo = aroundpositions(elfoslist, pos)
      #print(elfo, pos, aroundelfo, set(aroundelfo), set(aroundelfo) != {0})
      if set(aroundelfo) != {0}:
        havemoved = False
        for d in directions:
          if checkdirection(d, aroundelfo):
            #Move to direction
            elfosnew[elfo] = newposition(d, pos)
            #print(elfos[elfo], elfosnew[elfo], d)
            havemoved = True
            break

        if not havemoved:
          elfosnew[elfo] = pos

      else:
        elfosnew[elfo] = pos
      
    
    #print("elfos:", elfos)
    #print("elfosnew:", elfosnew)

    #Check if there is a colision - add the position to a list
    elfoscol = elfosnew.copy()
    for elfo in range(1, len(elfoscol) +1):
      pos = elfoscol.get(elfo)
      colisions = [k for k, v in elfoscol.items() if v == pos] # and k != elfo]
      #print(colisions)
      for c in colisions:
        if len(colisions)>1:
          elfosnew[c] = elfos[c]
        elfoscol.pop(c)

      #elfosnew[elfo] = elfos[elfo]
      #elfoscol.pop(elfo)
      

    """#collisions = [k for k, v in elfosnew.items() if sum(1 for v1 in elfosnew.values() if v1 == v) > 1]
    collisions = [k for k, v in elfosnew.items() if countOf(elfosnew.values(), v) > 1]
    for c in collisions:
      elfosnew[c] = elfos[c]"""
    
    """for elfo, pos in elfosnew.items():
      colisions = list(k for k, v in elfosnew.items() if v == pos)
      #print(colisions)
      if len(colisions) > 1:
        for c in colisions:
          elfosnew[c] = elfos[c]"""
        
    """if list(elfosnew.values()).count(pos) > 1:
      #print("Colision:",n , elfo, pos)
      for elfo2, pos2 in elfosnew.items():
        if pos2 == pos:
          elfosnew[elfo2] = elfos[elfo2]
      
      #print("despues de colision", elfosnew)
    """  
    
    directions = directions[1:] + directions[0]
    elfos, elfosnew = elfosnew, {}
    #print(elfos)
    #break

  
  #print(elfos)

  minx, maxx, miny, maxy = 9999, -9999, 9999, -9999
  for elfo, pos in elfos.items():
    if pos[0] < minx:
      minx = pos[0]
    if pos[0] > maxx:
      maxx = pos[0]
    if pos[1] < miny:
      miny = pos[1]
    if pos[1] > maxy:
      maxy = pos[1]

  
  result = (((maxx - minx)+1) * ((maxy - miny)+1)) - len(elfos)
  print("X range:", minx, maxx, "Y range:", miny, maxy, "Result:", result)

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = 0

  elfos, elfosnew = {}, {}
  elfos = parseinput(input)
  #print (elfos)

  directions = "NSWE"
  newround, toltalrounds = True, 0

  time = datetime.now()

  while newround:
    movedelfos = 0
    elfoslist = list(elfos.values()) 
    for elfo, pos in elfos.items():
      #Check all positions around the elfo
      aroundelfo = aroundpositions(elfoslist, pos)
      if set(aroundelfo) != {0}:
        havemoved = False
        for d in directions:
          if checkdirection(d, aroundelfo):
            #Move to direction
            elfosnew[elfo] = newposition(d, pos)
            #print(elfos[elfo], elfosnew[elfo], d)
            havemoved = True
            movedelfos += 1
            break

        if not havemoved:
          elfosnew[elfo] = pos

      else:
        elfosnew[elfo] = pos
      
    
    #print("elfos:", elfos)
    #print("elfosnew:", elfosnew)

    #Check if there is a colision - add the position to a list
    #elfosvalues = list(elfosnew.values())
    elfoscol = elfosnew.copy()
    for elfo in range(len(elfoscol.keys())):
      pos = elfoscol.get(elfo)
      colisions = [k for k, v in elfoscol.items() if v == pos] # and k != elfo]
      for c in colisions:
        if len(colisions)>1:
          elfosnew[c] = elfos[c]
        elfoscol.pop(c)
        
    """#collisions = [k for k, v in elfosnew.items() if sum(1 for v1 in elfosnew.values() if v1 == v) > 1]
    collisions = [k for k, v in elfosnew.items() if countOf(elfosnew.values(), v) > 1]
    for c in collisions:
      elfosnew[c] = elfos[c]"""
    
    """for elfo, pos in elfosnew.items():
      colisions = [k for k, v in elfosnew.items() if v == pos]
      #print(colisions)
      if len(colisions) > 1:
        for c in colisions:
          elfosnew[c] = elfos[c]
    """
    """if elfosvalues.count(pos) > 1:
      while True:
        try:
          index = elfosvalues.index(pos)
          elfosnew[index] = elfos[index]
          elfosvalues[index] = elfos[index]
        except:
          break
    """
      

        #print("despues de colision", elfosnew)
        
    
    directions = directions[1:] + directions[0]
    elfos, elfosnew = elfosnew, {}
    #print(elfos)

    newround = movedelfos != 0
    toltalrounds += 1
    if toltalrounds % 50 == 0:
      print(toltalrounds, newround, movedelfos, "Diff:", datetime.now()-time)
      time = datetime.now()

  
  result = toltalrounds

  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""
sampleexpetedresultone = 110
sampleexpetedresulttwo = 20

file = open("day23.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

start = datetime.now()
sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
end = datetime.now()
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)
print("Start:", start, "End:", end, "Diff:", end - start)

assert solveparttwo(sampleinput) == sampleexpetedresulttwo

start = datetime.now()
sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
end = datetime.now()
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)
print("Start:", start, "End:", end, "Diff:", end - start)
