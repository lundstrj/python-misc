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

class CLASSNAME(object):
  debug = False
  
  def main(self):
    pass

  def init(self):
    pass
        
if __name__ == "__main__":
  run = CLASSNAME()
  run.init()
  run.debug = True
  run.main()
