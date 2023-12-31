from hashlib import md5

def solvepartone(input):

  result = 0

  #print(md5(input.encode()).hexdigest())

  while True:
    
    key = md5((input + str(result)).encode()).hexdigest()

    if key.startswith('00000'):
      print(key)
      break

    result +=1

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input, min):

  result = min

  #print(md5(input.encode()).hexdigest())

  while True:
    
    key = md5((input + str(result)).encode()).hexdigest()

    if key.startswith('000000'):
      print(key)
      break

    result +=1

  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """abcdef"""
sampleexpetedresultone = 609043
sampleexpetedresulttwo = 0

file = open("day04.txt", "r")
input = file.read()

assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)

#assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = 0 #solveparttwo(sampleinput)
result = solveparttwo(input, result)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)