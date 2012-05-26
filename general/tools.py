def argv_handler(argv, debug=False):
  if not "str" in str(type(argv)):
    pass
  else: argv = argv.split()    
  out = {}
  skip_next = False
  if debug: print argv
  for arg in argv:
    if skip_next:
      skip_next=False
      continue
    if '-' in arg:
      if '-' in argv[argv.index(arg)+1]:
        out[arg] = True
      else:
        out[arg] = argv[argv.index(arg)+1]
        skip_next = True
  return out

def prop_argv_handler(string): # TDD FTW!
  return argv_handler("-t -v -d -f olle.txt -x -g jadajada") == {'-d': True, '-g': 'jadajada', '-f': 'olle.txt', '-t': True, '-v': True, '-x': True}

def boolkey(dic, key):
  if dic.has_key(key): return dic[key]
  else: return False

if __name__ == "__main__":
  import sys
  print ":Tools:"
  print prop_argv_handler("")
  print argv_handler(sys.argv, debug=True)
