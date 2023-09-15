def parseinput(input):
  
  rows = input.splitlines()
  count = len(rows)
  original = {}
  list = []

  for i in range(len(rows)):
    #original[i] = str(i)+'|'+str(rows[i])
    list.append(str(i)+'|'+str(rows[i]))
  
  return list, count


def parseinput2(input):
  
  rows = input.splitlines()
  count = len(rows)
  list = []

  for i in range(len(rows)):
    #original[i] = str(i)+'|'+str(rows[i])
    list.append(str(i)+'|'+str(int(rows[i])*811589153))
  
  return list, count


def solvepartone(input):

  result = 0

  list, count = parseinput(input)
  original = list.copy()


  print(count)

  for i in range(count):
    #print("Orig:", i, original[i])
    for j in range(count):
      if original[i] == list[j]:
        val = list[j]
        newpos = j + (int(val[val.find('|')+1:]) % (count-1))
        if newpos == j:
          break
        elif newpos <= 0:
          newpos = (count-1) + newpos
        elif newpos > (count-1):
          newpos = newpos - (count-1)
        
        #print(val, i, j, newpos)
        list.pop(j)
        list.insert(newpos, val)
        #print(list)
        
        break
    

  #print(original, list)
  pos0 = 0
  for i in range(count):
    row = list[i]
    if int(row[row.find('|')+1:]) == 0:
      pos0 = i
      break

  first = list[(1000 + pos0) % count]
  second = list[(2000 + pos0) % count]
  third = list[(3000 + pos0) % count]
  print('Pos 0:', pos0, 'First:', first, 'Second:', second, 'Third:', third)

  result = int(first[first.find('|')+1:]) + int(second[second.find('|')+1:]) + int(third[third.find('|')+1:])

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):


  result = 0

  list, count = parseinput2(input)
  original = list.copy()


  print(count)

  for a in range(10):
    for i in range(count):
      #print("Orig:", i, original[i])
      for j in range(count):
        if original[i] == list[j]:
          val = list[j]
          newpos = j + (int(val[val.find('|')+1:]) % (count-1))
          if newpos == j:
            break
          elif newpos <= 0:
            newpos = (count-1) + newpos
          elif newpos > (count-1):
            newpos = newpos - (count-1)
          
          #print(val, i, j, newpos)
          list.pop(j)
          list.insert(newpos, val)
          #print(list)
          
          break
      

  #print(original, list)
  pos0 = 0
  for i in range(count):
    row = list[i]
    if int(row[row.find('|')+1:]) == 0:
      pos0 = i
      break

  first = list[(1000 + pos0) % count]
  second = list[(2000 + pos0) % count]
  third = list[(3000 + pos0) % count]
  print('Pos 0:', pos0, 'First:', first, 'Second:', second, 'Third:', third)

  result = int(first[first.find('|')+1:]) + int(second[second.find('|')+1:]) + int(third[third.find('|')+1:])

  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# Start calling the function
sampleinput = """1
2
-3
3
-2
0
4"""
sampleexpetedresultone = 3
sampleexpetedresulttwo = 1623178306

file = open("day20.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)