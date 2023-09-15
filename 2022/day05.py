def setStacks(group):
  
  stacks = []
  col = 0

  # Work with the fisrt group to determine the intial state
  rows = group.splitlines()
  
  for j in range(0,len(rows[0]),4):
    stacks.append('')

    for i in range(len(rows)-1,0,-1):
      crate = rows[i-1][j:j+3].replace('[','').replace(']','').strip()

      if crate != '':
        stacks[col] = stacks[col] + crate
    
    col = col + 1

  return stacks


def solvepartone(input):

  result = ""
  stacks = []

  groups = input.split('\n\n')
  #print(groups[0])

  # Use a function to create the original map
  stacks = setStacks(groups[0])


  # Work with the second group manage the moves
  #print(groups[1])
  rows = groups[1].splitlines()

  print(stacks)

  for r in rows:
    move = r.replace('move ','').replace('from ','').replace('to ','').split()
    #print(move)

    stacks[int(move[2])-1] = stacks[int(move[2])-1] + stacks[int(move[1])-1][-int(move[0])::-1]
    stacks[int(move[1])-1] = stacks[int(move[1])-1][:-int(move[0])]

    #for c in range(0,int(move[0])):
    #  stacks[int(move[2])-1] = stacks[int(move[2])-1] + stacks[int(move[1])-1][-1:]
    #  stacks[int(move[1])-1] = stacks[int(move[1])-1][:-1]

    print(stacks)
  
  for c in stacks:
    result = result + c[-1:]

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = ""
  stacks = []

  groups = input.split('\n\n')
  #print(groups[0])

  # Use a function to create the original map
  stacks = setStacks(groups[0])


  # Work with the second group manage the moves
  #print(groups[1])
  rows = groups[1].splitlines()

  for r in rows:
    move = r.replace('move ','').replace('from ','').replace('to ','').split()
    #print(move)

    stacks[int(move[2])-1] = stacks[int(move[2])-1] + stacks[int(move[1])-1][-int(move[0]):]
    stacks[int(move[1])-1] = stacks[int(move[1])-1][:-int(move[0])]

    #print(stacks)
  
  for c in stacks:
    result = result + c[-1:]


  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
sampleexpetedresultone = "CMZ"
sampleexpetedresulttwo = "MCD"

file = open("day05.txt", "r")
input = file.read()

sampleresult = solvepartone(sampleinput)
result = "" #solvepartone(input)

print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


sampleresult = solveparttwo(sampleinput)
result = "" #solveparttwo(input)

print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)