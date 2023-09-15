def getDirs(input):

  result = 0
  dir = ''
  path = ''
  dirs = dict()

  rows = input.splitlines()
  
  
  for r in rows:
    if r.find('$ ls') != -1:
      pass
    elif r.find('$ cd') != -1:
      dir = r[5:]
    
      if dir != '..': # if it is a valid dir
        # Look for directory by name 
        path = path + dir + '|'
        dirs[path] = 0
      else: # It is .. and we need to look for the parent directory
        dir = path.split('|')[-2]
        path = path.removesuffix(dir + '|')

    else:
      data = r.split()
      if data[0] == 'dir':
        pass
      else:
        dirs[path] = int(dirs[path]) + int(data[0])
    

  for path in dirs.keys():
    for path2, val2 in dirs.items():
      if path != path2 and path2.find(path) != -1:
        dirs[path] = dirs[path] + val2
  

  return dirs


def solvepartone(input):

  result = 0
  
  dirs = getDirs(input)
  #print(dirs)

  for val in dirs.values():
    if val <= 100000:
      result = result + val
  

  return result

# ----------------------------------------------------------------------------

def solveparttwo(input):

  dirs = getDirs(input)
  #print(dirs)

  need = 30000000 - (70000000 - dirs.get('/|',0))
  result = 70000000
  #print('Need:',need)

  for val in dirs.values():
    if val >= need and val < result:
      result = val

  
  return result


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


# Start calling the function
sampleinput = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
sampleexpetedresultone = 95437
sampleexpetedresulttwo = 24933642

file = open("day07.txt", "r")
input = file.read()

sampleresult = solvepartone(sampleinput)
result = solvepartone(input)

print("Part One -> Expected Result:", sampleexpetedresultone, "- Result:", sampleresult, "- Input Result:", result)


sampleresult = solveparttwo(sampleinput)
result = solveparttwo(input)

print("Part Two -> Expected Result:", sampleexpetedresulttwo, "- Result:", sampleresult, "- Input Result:", result)