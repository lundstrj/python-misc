import sys, time
from time import gmtime, strftime

try:
  import curses
except:
  print "Failed to load curses"

def draw_ascii_spinner(spin_time=None, delay=0.2):
  """
  if curses_enabled:
    stdscr = curses.initscr()
    curses.noecho()
    spi = ['  . .\n.   .\n. . .\n','.   .\n.   .\n. . .\n','. .  \n.   .\n. . .\n','. . .\n.    \n. . .\n','. . .\n.   .\n. .  \n','. . .\n.   .\n.   .\n','. . .\n.   .\n  . .\n','. . .\n    .\n. . .\n','. . .\n.   .\n. . .\n']

    i = 0
    while i < 20:
      i+=1
      for c in spi:
        stdscr.addstr(0,0,c)
        stdscr.refresh()
        time.sleep(0.2)
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    time.sleep(1)
    curses.endwin()
    sys.exit()  
    """
  
  try:
    start_clock = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    times_total = 50000
    if spin_time: times_total = int(spin_time/delay)
    counter = 0
    stri = ""
    minute = 60
    hour = 60*60
    seconds = 0
    
    spinner1 = '/-\|'
    spinner2 = '[|]'
    spinner3 = '_-='
    spinner4 =  ['......',' .....','.. ...','... ..','.... .','..... ']
    spinner5 = [' .\n..','. \n..','..\n. ','..\n .']

    while counter < times_total:
      for char in spinner4: # there should be a backslash in here.
        if delay < 1: seconds = counter*delay
        else: seconds = counter/delay
        h = str(int(seconds/hour))   
        rest = seconds%hour
        m = str(int(rest/minute))
        s = str(int(rest)%minute)
        if (int(h) > 0): stri = " "+h+"h"+m+"m"+s+"s "
        elif (int(seconds) > minute): stri = " "+m+"m"+s+"s "
        else: stri = " "+s+"s "
        sys.stdout.write(char+stri)
        #sys.stdout.write(char)
        #sys.stdout.write(stri)
        counter+=1
        sys.stdout.flush()
        time.sleep(0.2) # time.sleep(0.2) # Debug code
        sys.stdout.write('\r') # this should be backslash r.
        #sys.stdout.write('\r') # this should be backslash r.
    end_clock = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print "total time: %s started: %s finished: %s" % (stri[1:-1], start_clock, end_clock)
    return int(seconds)
  except:
    print "\nunexpected failure in the spinner, someone should look at that"
print draw_ascii_spinner()
  
