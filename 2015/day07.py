def parseinput(input : str):
  
  rows = input.splitlines()
  inst = {}
  for r in rows:
    opp, wire = r.split(' -> ')
    vals = []
    for n in opp.split():
      vals.append(n)

    inst[wire] = vals
  
  return inst

def notval(num : int):
  
  bina = bin(num)
  num = ('0' * (18-len(bina))) + bina[2:]
  #print(bina, num, int(num,2))
  notnum = ''
  for n in num:
    notnum += str(int(n) ^ 1)
    
  return int(notnum, 2)


def solvewire(circuits : list(), wire : str):
  
  if wire.isnumeric():
    return int(wire)
  
  wireval = circuits[wire]
  #print(wire, wireval)

  # IF there is only one value it is already calculated
  if len(wireval) == 1:
    value = solvewire(circuits, wireval[0])
    #return solvewire(circuits, wireval[0])

  elif len(wireval) == 2:
    # Its a NOT
    value = notval(solvewire(circuits, wireval[1]))
    #return notval(solvewire(circuits, wireval[1]))
  
  else:
    
    if wireval[1][1:] == 'SHIFT':
      val = solvewire(circuits, wireval[0])
      if wireval[1][0:1] == 'L':
        value = val << int(wireval[2])
        #return val << int(wireval[2])
      else:
        value = val >> int(wireval[2])
        #return val >> int(wireval[2])

    else:
      val = solvewire(circuits, wireval[0])
      val2 = solvewire(circuits, wireval[2])

      if wireval[1] == 'OR':
        value = val | val2
        #return val | val2
      else:
        value = val & val2
        #return val & val2
  
  #if wire == 'a': 
  #  print(value, wireval, wire)
  circuits[wire] = [str(value)]
  
  return value



def solvepartone(input : str, wire : str):

  result = 0

  circuits = parseinput(input)
  #print(circuits)
  #print(circuits['r'])

  result = solvewire(circuits, wire)


  return result

# ----------------------------------------------------------------------------

def solveparttwo(input : str, wire : str, overridewire : str):

  result = 0

  circuits = parseinput(input)
  #print(circuits)
  #print(circuits['r'])
  
  firstcircuits = circuits.copy()
  wirevalue = solvewire(firstcircuits, wire)

  circuits[overridewire] = [str(wirevalue)]

  result = solvewire(circuits, wire)
  
  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""
sampleexpetedresultone = 72
sampleexpetedresulttwo = 72

file = open("day07.txt", "r")
input = file.read()

#print(notdec(456))
assert solvepartone(sampleinput, 'd') == 72
assert solvepartone(sampleinput, 'e') == 507
assert solvepartone(sampleinput, 'f') == 492
assert solvepartone(sampleinput, 'g') == 114
assert solvepartone(sampleinput, 'h') == 65412
assert solvepartone(sampleinput, 'i') == 65079

#assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput, 'd')
result = solvepartone(input, 'a')
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput, 'd', 'd') == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput, 'd', 'd')
result = solveparttwo(input, 'a', 'b')
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)