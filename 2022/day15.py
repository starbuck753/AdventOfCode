def printmap(sensors, beacons, minx, maxx, miny, maxy):

  for y in range(int(miny), int(maxy)):
    line = ''
    for x in range(int(minx), int(maxx)):
      c = '.'
      if str(x)+','+str(y) in sensors:
          c = 'S'
      if str(x)+','+str(y) in beacons:
          c = 'B'

      line += c

    print(line)

  return

def parseinput(input, line):

  sensors, beacons, distances, sensorsdist = [], [], [], []
  xs, ys = set(), set()

  rows = input.splitlines()
  
  for r in rows:
    sen, bea = r.replace(' ','').replace('Sensoratx=','').replace('closestbeaconisatx=','').replace('y=','').split(':') #Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    sensors.append(sen)
    beacons.append(bea)

    x, y = sen.split(',')
    x1, y1 = bea.split(',')
    x, y, x1, y1 = int(x), int(y),int(x1), int(y1)
    dist = abs(x-x1)+abs(y-y1)

    if (line - y <= dist) or line == 0:
      xs.add(x+dist)
      xs.add(x-dist)
      ys.add(y+dist)
      ys.add(y-dist)
    else:
      xs.add(x)
      ys.add(y)
      #xs.add(x1)
      #ys.add(y1)
    
    distances.append(dist)
    #sensorsdist.append(sen+','+str(dist))

  return sensors, beacons, distances, xs, ys

def solvepartone(input, line, printit):

  result = 0

  sensors, beacons, distances, xs, ys = parseinput(input, line)
  ubeas = set(beacons)
  #print(sensors, beacons, ubeas, xs, ys)

  #Gen Min and max x and y
  minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
  print(minx, maxx)


  if printit:
    printmap(sensors, beacons, minx, maxx, miny, maxy)


  #Get the sensors that are near the cheking line
  cline = ''
  for col in range(int(minx), int(maxx)):
    c = '.'

    for i in range(len(sensors)):
      x, y = sensors[i].split(',')

      #If distance from sensor to the checking point is less than the sensor distance then the space is free
      if(distances[i] >= (abs(col-int(x))+abs(line-int(y)))): # and (str(col) + ',' + str(line) != beacons[i]):
        c = '#'
        break

    if (str(col) + ',' + str(line)) in ubeas:
      c = '.'

    cline += c
  
  if printit:
    print(cline)
  
  result = cline.count('#')

  print(cline.count('.'), cline.count('#'),abs(minx)+maxx, cline.count('.')+cline.count('#'))
  print(result)

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input, maxval):

  result = 0

  sensors, beacons, distances, xs, ys = parseinput(input, 0)
  ubeas = set(beacons)
  #print(sensors, beacons, ubeas, xs, ys)

  #Gen Min and max x and y
  #minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
  #print(minx, maxx)

  for line in range(int(maxval)):
    #cline = ''
    ranges = []

    for i in range(len(sensors)):
      x, y = sensors[i].split(',')

      dist = abs(int(y) - line)
      print(line, dist, x, y, distances[i])
      if dist <= distances[i]:
        x0, x1 = int(x) -(distances[i] - dist), int(x) +(distances[i] - dist)
        isfound = False
        
        for j in range(len(ranges)):
          rx0, rx1 = ranges[j].split(',')
          if (x0 <= int(rx0) and x1 >= int(rx0)) or (x1 >= int(rx1) and x0 <= int(rx1)):
            ranges[j] = str(min(x0,int(rx0)))+','+str(max(x1,int(rx1)))
            isfound = True
          elif x0 >= int(rx0) and x1 <= int(rx1):
            isfound = True
            
        
        if not isfound or len(ranges) == 0:
          ranges.append(str(x0)+','+str(x1))


    for bea in ubeas:
      x, y = bea.split(',')

      if line == int(y):
        isfound = False
        
        for j in range(len(ranges)):
          rx0, rx1 = ranges[j].split(',')
          if (int(x) >= int(rx0) and int(x) <= int(rx1)):
            ranges[j] = str(min(int(x),int(rx0)))+','+str(max(int(x),int(rx1)))
            isfound = True
        
        if not isfound or len(ranges) == 0:
          ranges.append(x+','+x)
    

    uranges = set(ranges)
    if len(uranges) > 1:
      print(line, uranges, ranges)


  #print(cline.count('.'), cline.count('#'),abs(minx)+maxx, cline.count('.')+cline.count('#'))
  print(result)

  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
sampleexpetedresultone = 26
sampleexpetedresulttwo = 56000011

file = open("day15.txt", "r")
input = file.read()

assert solvepartone(sampleinput, 10, 1) == sampleexpetedresultone

#sampleresult = solvepartone(sampleinput, 10, 0)
#result = solvepartone(input, 2000000, 0)
#print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


assert solveparttwo(sampleinput, 20) == sampleexpetedresulttwo

sampleresult = solveparttwo(sampleinput, 20)
result = solveparttwo(input, 4000000)
print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)