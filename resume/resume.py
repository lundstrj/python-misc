#!/usr/bin/env python
# Written by Johan Lundstrom
# Date: 18/5/2011
# E-mail: lundstrom.se@gmail.com
#
# Usage: 

import sys
import os
import time
class resume(object):
  debug = False
  interactive = False
  test = False
  file_name = ''
  #bold = "\033[1m"
  #reset = "\033[0;0m"
  #bold = os.popen('tput bold').read()
  bold = os.popen('tput setaf 1').read()
  reset = os.popen('tput sgr0').read()
  bold_set = False
  
  string = """Johan Lundstrom 
lundstrom.se@gmail.com, +46 (0)72 734 4108
Inlandsgatan 31D,  417 15 Gothenburg, Sweden 

#Objective#
To solve interesting problems and to be challenged by the highest levels of self-reliance, resourcefulness and teamwork.

Experience 
Sogeti, Gothenburg, Test expert and Software Developer 
September 2010 ~ Present 
I was hired to help develop the local Sogeti branch as a test excellence center. Sogeti is a really great employer that have allowed me 
to gain insight into how a really big corporations handle IT and software projects. 

Nicira, Palo Alto, CA, MTS Intern 
May 2009 ~ April 2010 
Developed and extended the in-house custom automation harness. Gained invaluable programming skills in python and extensive know how in 
how to build automation systems. Because of the start-up nature of the company I had to work in the entire stack, from hardware debugging 
to high level software design and integration of different open source systems. I programmed mostly in Python but also used shell 
scripting and some php. Since Nicira is in the packet switched network field, I became quite proficient in debugging networks. Nicira was 
also humbling for me, being in an environment with so many rockstars who still were so genuinely helpful in bringing me up to speed is 
something not everyone gets to experience. 

Chalmers University of Technology, Gothenburg, Software Developer Consultant 
January 2009 - May 2009 
After the thesis work for Qualisys was done, the university wanted to continue development so I signed on to bring a PhD up to speed on 
the algorithms, the code base and how to set it up properly. We wrote a paper based on our work that published and got accepted at the 

IDETC/CIE conference in San Diego 2009. 
Qualisys, Gothenburg, Thesis worker 
May 2008 ~ January 2009 
Developed a real time system for marker position prediction in 3D.The task was to deliver a system that could be shipped to customers and 
we delivered a one button system that could bridge gaps of several seconds without the user noticing. Build in C++, Python and Tcl/Tk. 
Please, ask me about this at the interview. 

Volvo Trucks, Gothenburg, Summer intern, Software tools and development 
May 2007 - September 2007 
Gave feedback on early versions of an internal system for programming trucks. Reported bugs, interacted with developers to discuss 
solutions and to define the desired behavior of the product. 

The Royal Swedish Air Force, Kallinge, Squad Leader in a reconnaissance ground unit (mandatory service) 
August 2003 - May 2004 
Got my can do attitude during this year. There are things you simply can not learn in any other place than the armed forces and I am 
truly privileged to have been picked for this task.  

Capabilities 
   * Strong problem solving skills, if you give me the authority, I will solve the task.
   * Team player above all. It's not about what I can do, it's about what we can do. 
   * Eyes on the target at all times. Tasks must bring us closer to the goal. 
   * I get my hands dirty, no questions asked. What needs to get done simply needs to get done. We need a piece of hardware to get something done? I'll figure out how to get it in time. 
   * I anticipate change at all times. Unexpected things will happen, what matters is how you deal with it. 
   * A can do attitude. Of course we can do that! 
   * Hands on experience with common tools such as: SVN, git, redmine, testlink, eclipse, vi, wireshark, tcpdump. 
   * I'm a Python hacker that used to be a Java hacker. 
   * I'm a start up engineer. I don't always go by the book. 

Education 
Chalmers University of Technology, Gothenburg, Sweden 
MSc in Software Engineering 
August 2004 ~ August 2011 (expected) 
The university gave me a lot of theoretical skills in maths and science while also providing a brief insight into a lot of programming 
languages such as: ASP, PHP, HTML, XML, SQL, C, C++, Assembler, Java, Haskell and MPD. It also introduced concepts such as different 
agile methods (XP, scrum, crystal, etc.), development patterns and architectures such as (Model-View-Controller, pipes and filters, etc) 
and finally processes such as LEAN, the V-model, waterfall and so on. Having heard of all of these things, I have an easier time 
evaluating the best approach for the problem I'm facing at the moment. Chalmers didn't give me all the answers but it gave me a vague 
idea of how much there is to learn. 

Commission of trust and miscellaneous 

Editor in Chief for TraineeReport 2007 and board member in CETAC 2008 (www.cetac.se) 
In my spare time I sometimes meet up with the Phantom to fight crime and such."""
  def main(self):
    self.flowPrint(self.string)
  
  def flowPrint(self, text):
    for char in text:
      if char == '#' and self.bold_set:
        self.bold_set = False
        sys.stdout.write(self.reset)
        print "reset"
        continue
      if char == '#' and not self.bold_set:
        self.bold_set = True
        sys.stdout.write(self.bold)
        print "setting bold"
        continue
        
      sys.stdout.write(char)
      time.sleep(0.01)
	
  def tagHandler(self, text, index):
    pass
    
	
if __name__ == "__main__":
	t = resume()
	t.main()