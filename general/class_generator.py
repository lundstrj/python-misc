"""
Author: Johan Lundstroem
Email: lundstrom.se at gmail.com
Date: 12/9 2011
License: GPLv2
"""

import __init__
import subprocess
import sys
import time
import tools

class ClassGenerator(object):
  debug = False
  file_path = ""
  class_name = ""
  
  def main(self, argd):
    if len(argd) == 0:
      self.print_class()
    else:
      pass
      

  def init(self):
    pass

if __name__ == "__main__":  
  help_str = "Usage: -n <class_name>\n       -d (debug)\n       -t <target path>\n"\
        "       -h (print help)"
  argd = tools.argv_handler(sys.argv)
  if tools.boolkey(argd, '-h'):
    print help_str
    sys.exit()
  run = ClassGenerator()
  run.init()
  run.debug = True
  run.main(argd)
