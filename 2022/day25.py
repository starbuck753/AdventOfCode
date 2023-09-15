
def parseinput(input):
  
  rows = input.splitlines()
  maxd = 0
  numbers, digit = [], []

  for r in rows:
    numbers.append(r[::-1])
    if len(r) > maxd: 
      maxd = len(r)

  for d in range(maxd):
    num = ''
    for n in numbers:
      if len(n) > d:
        num += n[d]
    
    digit.append(num)
  
  return digit


def valtosnafu(val, rest=0):
  if val == 3:
    val = "="
    rest += 1
  if val == 4:
    val = "-"
    rest += 1
  if val == -1:
    val = "-"
  if val == -2:
    val = "="
  if val == -3:
    val = "2"
    rest -= 1
  if val == -4:
    val = "1"
    rest -= 1
  if val == 5:
    val = "0"
    rest += 1
  
  return str(val), rest


def solvepartone(input):

  result = 0

  digits = parseinput(input)
  print(digits)
  total, rest = "", 0

  for digit in digits:
    val = rest
    rest = 0
    val, rest = valtosnafu(val)

    #print("1. Val:", val, "Rest:", rest)
    digit += str(val)
    
    # Sum all the digits
    sum = 0
    sum += digit.count('2') * 2
    sum += digit.count('1')
    sum += digit.count('-') * -1
    sum += digit.count('=') * -2

    
    # Determine the value and the rest for the next digit
    rest += int(sum/5)
    val = abs(sum)%5 
    if sum < 0 : val = val *(-1)
    #print("2. Sum:", sum, "Rest:", rest, "Val:", val)

    val, rest = valtosnafu(val, rest)

    
    total += str(val)
    #print("3. Tot:", total, "Sum:", sum, "Rest:", rest, "Val:", val, digit)

  print("Rest", rest)
  if rest > 0:
    val, _ = valtosnafu(rest)
    total += val

  print("Final Value:", total[::-1])
  result = total[::-1]

  return result


# ----------------------------------------------------------------------------

def snafutodec(num):

  num = num[::-1]
  pos, val = 0, 0
  for d in num:
    if d == '-':
      n = -1
    elif d == '=':
      n = -2
    else:
      n = int(d)

    val += n * (5 ** pos)
    pos += 1
  
  #print(num[::-1], val)
  return val

def dectosnafu(num):

  num = str(num)[::-1]
  total, val, rest = '', '', 0

  for d in num:
    d = int(d)
    nums = []
    val = rest
    rest = 0
    val, rest = valtosnafu(val, rest)

    nums.append(val)
    #print("1. Val:", val, "Rest:", rest)
    
    rest += int(d/5)
    val = abs(d)%5 
    if d < 0 : val = val *(-1)
    #print("2. Sum:", d, "Rest:", rest, "Val:", val)

    val, rest = valtosnafu(val, rest)

    nums.append(val)
    sum = 0
    for n in nums:
      if n == '2':
        sum += 2
      if n == '1':
        sum += 1
      if n == '0':
        pass
      if n == '-':
        sum -= 1
      if n == '=':
        sum -= 2
      #print(n,sum)

    val, _ = valtosnafu(sum)
    total += val
    print("3. Tot:", total, "Sum:", sum, "Rest:", rest, "Val:", val, nums)

  if rest > 0:
    val, _ = valtosnafu(rest)
    total += val

  total = total[::-1]
  print(total)
  
  return total

def solvepartone2(input):

  result = 0

  numbers = input.splitlines()
  decnumber = 0

  for num in numbers:
    decnumber += snafutodec(num)
  
  print(decnumber)

  result = dectosnafu(decnumber)

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  result = 0

  parseinput(input)



  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""
sampleexpetedresultone = "2=-1=0"
sampleexpetedresulttwo = 0

#20===-20-020=0-01-02

file = open("day25.txt", "r")
input = file.read()

#2022 - 20 - 20 - 15 - 353 - 353 - 201 - 201 - 201 - 107 - 107 - 353 - 10 - 20- 15 - 20 - 10 - 7 - 6 - 3
anothersample = """1-0
1-0
1=0
1=-1=
1=-1=
2=01
2=01
2=01
1-12
1-12
1=-1=
20
1-0
1=0
1-0
20
12
11
1="""	

assert solvepartone(anothersample) == "1=11-2"



#assert snafutodec("1=-0-2") == 1747
#assert snafutodec("12111") == 906
#assert snafutodec("2=0=") == 198
#assert snafutodec("21") == 11
#assert snafutodec("2=01") == 201
#assert snafutodec("111") == 31
#assert snafutodec("20012") == 1257
#assert snafutodec("112") == 32
#assert snafutodec("1=-1=") == 353
#assert snafutodec("1-12") == 107
#assert snafutodec("12") == 7
#assert snafutodec("1=") == 3
#assert snafutodec("122") == 37


#assert dectosnafu(1) == "1"
#assert dectosnafu(2) == "2"
#assert dectosnafu(3) == "1="
#assert dectosnafu(4) == "1-"
#assert dectosnafu(5) == "10"
#assert dectosnafu(6) == "11"
#assert dectosnafu(7) == "12"
#assert dectosnafu(8) == "2="
#assert dectosnafu(9) == "2-"
#assert dectosnafu(10) == "20"
#assert dectosnafu(15) == "1=0"
#assert dectosnafu(20) == "1-0"
#assert dectosnafu(2022) == "1=11-2"
#assert dectosnafu(12345) == "1-0---0"
#assert dectosnafu(314159265) == "1121-1110-1=0"



assert solvepartone(sampleinput) == sampleexpetedresultone

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)
print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)
