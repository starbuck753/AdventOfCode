def solvepartone(input):

  result = 0

  rows = input.splitlines()
  
  cycles = (20, 60, 100, 140, 180, 220)
  signal = []

  cycle, x = 0, 1
  for r in rows:
    vals = r.split()

    #print(r, cycle, x)
    cycle += 1
    if cycle in cycles:
      signal.append(cycle * x)
    
    if vals[0] == "addx":
      cycle += 1
      if cycle in cycles:
        signal.append(cycle * x)
      x += int(vals[1])
    

  #print (signal)

  for val in signal:
    result += val  


  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = 0

  rows = input.splitlines()
  
  cycles = (40, 80, 120, 160, 200, 240)

  cycle, x, line = 0, 1, ""

  for r in rows:
    vals = r.split()
    #print(r, cycle, x)
    
    cycle += 1
    if cycle % 40 in [x, x+1, x+2]:
      line += "#"
    else:
      line += "."

    if cycle in cycles:
      print(line, "|")
      line = ""

    if vals[0] == "addx":
      cycle += 1
      if cycle % 40 in [x, x+1, x+2]:
        line += "#"
      else:
        line += "."

      if cycle in cycles:
        print(line, "|")
        line = ""

      x += int(vals[1])

    

  #print(crt)  
  print("")
  
  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
sampleexpetedresultone = 13140
sampleexpetedresulttwo = 0

file = open("day10.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)