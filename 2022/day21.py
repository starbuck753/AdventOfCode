def parseinput(input):
  
  rows = input.splitlines()
  monkeys = {}

  for r in rows:
    monkey, val = r.split(': ')
    monkeys[monkey] = val

  return monkeys


def solveMonkey(monkeys: dict[str, str], val: str)  -> int:

  monkeyval = 0

  if not val.isnumeric():
    monkey1, sign, monkey2 = val.split(' ')

    #Look for monkey1 and monkey2 and replace them for thier values
    val1 = solveMonkey(monkeys, monkeys[monkey1])
    val2 = solveMonkey(monkeys, monkeys[monkey2]) 

    if sign == '+':
      monkeyval = int(val1) + int(val2)
      #return int(val1) + int(val2)
    elif sign == '-':
      monkeyval = int(val1) - int(val2)
      #return int(val1) - int(val2)
    elif sign == '*':
      monkeyval = int(val1) * int(val2)
      #return int(val1) * int(val2)
    elif sign == '/':
      monkeyval = int(int(val1) / int(val2))
      #return int(int(val1) / int(val2))
      
  else:
    monkeyval = int(val)
    #return int(val)

  return monkeyval


def isHuman(monkeys: dict[str, str], val: str) -> bool:

  if val.isnumeric():
    return False
  
  monkey1, sign, monkey2 = val.split(' ')

  #Look for monkey1 and monkey2 and replace them for thier values
  if (monkey1 == 'humn' or monkey2 == 'humn'):
    return True

  if isHuman(monkeys, monkeys[monkey1]):
    return True
  
  return isHuman(monkeys, monkeys[monkey2])


def solveHuman(monkeys: dict[str, str], finalmonkey: str, monkey1: str, monkey2: str, sign: str, total: int) -> int:

  #print(monkey1, isHuman(monkeys, monkeys[monkey1]))
  #print(monkey2, isHuman(monkeys, monkeys[monkey2]))
  
  if not isHuman(monkeys, monkeys[monkey1]):
    # Calculates the value of monkey 1
    val = solveMonkey(monkeys, monkeys[monkey1])
    if sign == '+': #total = val + x
      val = int(total) - int(val)
    elif sign == '-': #total = val - x
      val = int(val) - int(total)
    elif sign == '*': #total = val * x
      val = int(total) / int(val)
    elif sign == '/': #total = val / x
      val = int(val) / int(total)    
    
    other = monkey2
  else:
    # Calculates the value of monkey 2
    val = solveMonkey(monkeys, monkeys[monkey2])
    if sign == '+': #total = x + val
      val = int(total) - int(val)
    elif sign == '-': #total = x - val
      val = int(total) + int(val)
    elif sign == '*': #total = x * val
      val = int(total) / int(val)
    elif sign == '/': #total = x / val
      val = int(total) * int(val)
    
    other = monkey1

  #print(val, other)

  if other == finalmonkey:
    return int(val)
  else:
    monkey1, sign, monkey2 = monkeys[other].split(' ')
    return solveHuman(monkeys, finalmonkey, monkey1, monkey2, sign, int(val))



def solvepartone(input):

  result = 0

  monkeys = parseinput(input)

  #print(monkeys)

  result = solveMonkey(monkeys, monkeys['root'])

  
  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = 0

  monkeys = parseinput(input)
  finalmonkey = ''

  for mon in monkeys:
    if 'humn' in monkeys[mon]:
      finalmonkey = mon
      break
      
  print('Final:', finalmonkey)

  monkey1, sign, monkey2 = monkeys['root'].split(' ')
  
  #print(monkey1, isHuman(monkeys, monkeys[monkey1]))
  #print(monkey2, isHuman(monkeys, monkeys[monkey2]))

  val = 0

  if not isHuman(monkeys, monkeys[monkey1]):
    # Calculates the value of monkey 1
    val = solveMonkey(monkeys, monkeys[monkey1])
    other = monkey2
  else:
    # Calculates the value of monkey 2
    val = solveMonkey(monkeys, monkeys[monkey2])
    other = monkey1

  #print(val, other)

  # Calculates all monkeys up to the Final Monkey -> The one that has a humn operation
  monkey1, sign, monkey2 = monkeys[other].split(' ')
  total = solveHuman(monkeys, finalmonkey, monkey1, monkey2, sign, val)
  print('Total:', total)

  # Calculates hmn solving the final monkey operation
  monkey1, sign, monkey2 = monkeys[finalmonkey].split(' ')
  
  if monkey1 != 'humn':
    # Calculates the value of monkey 1
    val = solveMonkey(monkeys, monkeys[monkey1])
    print(monkey1, val)
    if sign == '+': #total = val + x
      result = int(total) - int(val)
    elif sign == '-': #total = val - x
      result = int(val) - int(total)
    elif sign == '*': #total = val * x
      result = int(total) / int(val)
    elif sign == '/': #total = val / x
      result = int(val) / int(total)
  else:
    # Calculates the value of monkey 2
    val = solveMonkey(monkeys, monkeys[monkey2])
    print(monkey2, val)
    if sign == '+': #total = x + val
      result = int(total) - int(val)
    elif sign == '-': #total = x - val
      result = int(total) + int(val)
    elif sign == '*': #total = x * val
      result = int(total) / int(val)
    elif sign == '/': #total = x / val
      result = int(total) * int(val)
    
  print('Human:', result)

  #result = solveHuman(monkeys, val, other)

  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""
sampleexpetedresultone = 152
sampleexpetedresulttwo = 301

file = open("day21.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)