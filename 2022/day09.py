def domatrix(tailx, taily):

  for y in range(-7, -2):
    line = ""
    for x in range(-8, 14):
      car = "."
      for tail in range(0, len(tailx)):
        if tailx[tail] == x and taily[tail] == y:
          car = str(tail)
          break
      
      line += car
    
    print(line)
  
  print("---")


def istouching(headx, heady, tailx, taily):

  return abs(headx - tailx) <= 1 and abs(heady - taily) <= 1

def isdiagonallly(headx, heady, tailx, taily):

  return abs(headx != tailx) and abs(heady != taily)


def movetail(prev, cur):

  if prev > cur : 
    cur += 1
  else:
    cur -= 1

  return cur


def solvepartone(input):

  result = 0

  rows = input.splitlines()
  
  headx, heady = 0, 0
  tailx, taily = 0, 0
  pos = {'0|0'}

  for r in rows:
    dir, steps = r.split()
    if dir == 'R':
      movepos = 'x'
      movedir = 1
    elif dir == 'D':
      movepos = 'y'
      movedir = 1
    elif dir == 'L':
      movepos = 'x'
      movedir = -1
    else:   #if dir == 'U':
      movepos = 'y'
      movedir = -1

    for i in range(0, int(steps)):
      # Move Head to new position
      if movepos == 'x':
        headx = headx + movedir
      else:
        heady = heady + movedir

      #Move Tail (if it needs to)
      if not istouching(headx, heady, tailx, taily):
        if isdiagonallly(headx, heady, tailx, taily):
          # Moves diagonally
          tailx = movetail(headx, tailx)
          taily = movetail(heady, taily)
        else:
          # Moves up, down, left or right depending on where is the head
          if headx != tailx:
            tailx = movetail(headx, tailx)
          else:
            taily = movetail(heady, taily)
  

      #print(headx, heady, tailx, taily)
      pos.add(str(tailx)+'|'+str(taily))


  #print(pos)
  result = len(pos)

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = 0

  rows = input.splitlines()
  
  #headx, heady = 0, 0
  tailx, taily = [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]
  pos = {'0|0'}

  for r in rows:
    dir, steps = r.split()
    if dir == 'R':
      movepos = 'x'
      movedir = 1
    elif dir == 'D':
      movepos = 'y'
      movedir = 1
    elif dir == 'L':
      movepos = 'x'
      movedir = -1
    else:   #if dir == 'U':
      movepos = 'y'
      movedir = -1

    for i in range(0, int(steps)):
      # Move Head to new position
      if movepos == 'x':
        tailx[0] = tailx[0] + movedir
      else:
        taily[0] = taily[0] + movedir

      #Move Tail (if it needs to)
      for tail in range(1, len(tailx)):
        if not istouching(tailx[tail-1], taily[tail-1], tailx[tail], taily[tail]):
          if isdiagonallly(tailx[tail-1], taily[tail-1], tailx[tail], taily[tail]):
            # Moves diagonally
            tailx[tail] = movetail(tailx[tail-1], tailx[tail])
            taily[tail] = movetail(taily[tail-1], taily[tail])

          else:
            # Moves up, down, left or right depending on where is the head
            if tailx[tail-1] != tailx[tail]:
              # Moves up or down
              tailx[tail] = movetail(tailx[tail-1], tailx[tail])
            else:
              # Moves left or right
              taily[tail] = movetail(taily[tail-1], taily[tail])

        #print("step:", steps, i, "head:", tailx[0], taily[0], "tail:", tail, tailx[tail], taily[tail])     
      
      #if (int(steps)==17):
      #  domatrix(tailx, taily)
      
      pos.add(str(tailx[9])+'|'+str(taily[9]))


  #print(pos)
  result = len(pos)
  
  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
sampleinputtwo = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
sampleexpetedresultone = 13
sampleexpetedresulttwo = 36

file = open("day09.txt", "r")
input = file.read()

assert istouching(1,1,0,0) == True
assert istouching(2,0,0,0) == False

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinputtwo) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinputtwo)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)