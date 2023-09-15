def parseinput(input):
  
  
  
  
  return

def solvepartone(input):

  result = 0

  rows = input.splitlines()
  allcubes = set(rows)
  cubes = []
  totalfaces = 0
  
  for r in allcubes:
    curr = r.split(',')
    #print(curr)
    faces = 6
    for cub in cubes:
      if curr[0] == cub[0] and curr[1] == cub[1] and (int(curr[2]) == (int(cub[2]) + 1) or int(curr[2]) == (int(cub[2]) - 1)):
        faces -= 2
      if curr[0] == cub[0] and curr[2] == cub[2] and (int(curr[1]) == (int(cub[1]) + 1) or int(curr[1]) == (int(cub[1]) - 1)):
        faces -= 2
      if curr[1] == cub[1] and curr[2] == cub[2] and (int(curr[0]) == (int(cub[0]) + 1) or int(curr[0]) == (int(cub[0]) - 1)):
        faces -= 2

      #print(curr, cub, faces, curr[0], cub[0])

    totalfaces += faces
    cubes.append(curr)

  #print(totalfaces)
  result = totalfaces

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = 0

  rows = input.splitlines()
  
  for r in rows:
    break


  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""
sampleexpetedresultone = 64
sampleexpetedresulttwo = 0

file = open("day18.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)