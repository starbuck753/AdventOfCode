def getouttrees(input):
  
  rows = input.splitlines()
  return len(rows)*2 + len(rows[0])*2 - 4
  

def getvtrees(rows):

  vtrees = dict()
  
  for y in range(0, len(rows)):
    for x in range(0, len(rows[0])):
      vtrees[str(x)] = vtrees.get(str(x),'') + rows[y][x]  


  return vtrees


def solvepartone(input):

  rows = input.splitlines()
  leny, lenx = len(rows), len(rows[0])

  result = leny*2 + lenx*2 - 4  # Outside trees
  #print("lenx:", lenx, "leny:", leny)
  
  intrees = []
  vtrees = getvtrees(rows)

  
  for y in range(1, leny-1):
    line = ""
    for x in range(1, lenx-1):
      val = rows[y][x]
      visible = 0
      #print('x:', x, 'y:', y, 'val:', val) 

      # Horizontal
      trees = set(rows[y][:x])
      if max(trees) < val:
        visible = 1
      trees = set(rows[y][x+1:])
      if max(trees) < val:
        visible = 1

     
      # Vertical
      col = vtrees.get(str(x),'')
      trees = set(col[:y])
      if max(trees) < val:
        visible = 1
      trees = set(col[y+1:])
      if max(trees) < val:
        visible = 1      
      
      line = line + str(visible)

    intrees.append(line)
  

  #print(intrees)
  #print(vtrees)

  for line in intrees:
    result = result + line.count("1")

  return result

# ----------------------------------------------------------------------------

def getscore(trees, val):

  score = 0
  for t in trees:
    score = score + 1
    if  t >= val:
      break

  return score


def solveparttwo(input):

  result = 0

  rows = input.splitlines()
  leny, lenx = len(rows), len(rows[0])

  treescore = []
  vtrees = getvtrees(rows)


  for y in range(1, leny-1):
    line = []
    for x in range(1, lenx-1):
      val = rows[y][x]

      # Horizontal
      trees = rows[y][x-1::-1]
      tot = getscore(trees, val)
      #print(x, y, val, trees, "1:", getscore(trees, val), tot)
      
      trees = rows[y][x+1:]
      tot = tot * getscore(trees, val)
      #print(x, y, val, trees, "2:", getscore(trees, val), tot)
     
      # Vertical
      col = vtrees.get(str(x),'')
      trees = col[y-1::-1]
      tot = tot * getscore(trees, val) 
      #print(x, y, val, trees, "3:", getscore(trees, val), tot)
      
      trees = col[y+1:]
      tot = tot * getscore(trees, val)      
      #print(x, y, val, trees, "4:", getscore(trees, val), tot)
      
      line.append(tot)

    treescore.append(line)


  #print(rows)
  #print(vtrees)
  #print(treescore)


  for line in treescore:
    if result < int(max(line)):
      result = int(max(line))


  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """30373
25512
65332
33549
35390"""
sampleexpetedresultone = 21
sampleexpetedresulttwo = 8

file = open("day08.txt", "r")
input = file.read()

assert getouttrees(sampleinput) == 16
assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)
