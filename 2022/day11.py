class Monkey:

  items = []
  optype = ""
  opval = 0
  test = 0
  iftrue = 0
  iffalse = 0
  inspected = 0

  def __init__(self, id):
    self.id = id
  
  def __str__(self):
    return f"Monkey: {self.id}, Items: {self.items}, Inspected: {self.inspected}"


  def printall(self):
    return f"Monkey: {self.id}, Items: {self.items}, Inspected: {self.inspected}, Operation: {self.optype} {self.opval}, Test: {self.test}|{self.iftrue}|{self.iffalse}"


  def receiveitem(self, item):
    self.items.append(item)



def parsearinput(input):

  monkeys = []

  monkeylist = input.split('\n\n')

  for m in monkeylist:
    lines = m.splitlines()

    monkey = Monkey(lines[0].replace("Monkey ","").replace(":","").strip())
    
    # Items
    monkey.items = lines[1].replace("Starting items:","").replace(" ","").split(",")

    # Operation
    optype, opval = lines[2].replace("Operation: new = old","").strip().split()
    monkey.optype = optype
    monkey.opval = opval

    # Test
    monkey.test = lines[3].replace("Test: divisible by","").strip()
    monkey.iftrue = lines[4].replace("If true: throw to monkey","").strip()
    monkey.iffalse = lines[5].replace("If false: throw to monkey","").strip()

    monkeys.append(monkey)
    
  return monkeys


def getcommondivisor(monkeys):

  divisor = 1

  for monkey in monkeys:
    divisor *= int(monkey.test)

  return divisor


def solvepartone(input):

  result = 0
  monkeys = parsearinput(input)

  #for m in monkeys:
  #  print(m.printall())

  for i in range(1, 21):
    for monkey in monkeys:
      #print("Roound:", i, monkey)
      
      while len(monkey.items) > 0:
        # Inspect Item -> operation on worry level
        worry = int(monkey.items.pop(0))
        if monkey.optype == '+':
          worry += int(monkey.opval)
        else:
          if monkey.opval == "old":
            worry *= worry
          else:
            worry *= int(monkey.opval)
        
        # -> worry level divided by 3
        worry = int(worry / 3)

        # Test item
        if worry % int(monkey.test) == 0:
          # If true
          monkeys[int(monkey.iftrue)].receiveitem(worry)
        else:
          # If false
          monkeys[int(monkey.iffalse)].receiveitem(worry)
        
        monkey.inspected += 1
    
    
  #for m in monkeys:
  #  print(m)  

  inspected = []
  for m in monkeys:
    inspected.append(m.inspected)

  inspected.sort(reverse = True)
  result = inspected[0] * inspected[1]
  #print(inspected, result)
  
  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = 0
  monkeys = parsearinput(input)

  #for m in monkeys:
  #  print(m.printall())

  divisor = getcommondivisor(monkeys)

  for i in range(1, 10001):
    for monkey in monkeys:
      #print("Roound:", i, monkey)
      
      while len(monkey.items) > 0:
        # Inspect Item -> operation on worry level
        worry = int(monkey.items.pop(0))
        if monkey.optype == '+':
          worry += int(monkey.opval)
        else:
          if monkey.opval == "old":
            worry *= worry
          else:
            worry *= int(monkey.opval)
        
        # -> worry level module common
        worry = worry % divisor

        # Test item
        if worry % int(monkey.test) == 0:
          # If true
          monkeys[int(monkey.iftrue)].receiveitem(worry)
        else:
          # If false
          monkeys[int(monkey.iffalse)].receiveitem(worry)
        
        monkey.inspected += 1
    
    
  for m in monkeys:
    print(m)  

  inspected = []
  for m in monkeys:
    inspected.append(m.inspected)

  inspected.sort(reverse = True)
  result = inspected[0] * inspected[1]
  #print(inspected, result)

  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

sampleexpetedresultone = 10605
sampleexpetedresulttwo = 2713310158

file = open("day11.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)