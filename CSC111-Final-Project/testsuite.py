# ------------------------------------------------------
#   Team Name:RNR
#   Team Members:Rachel, Natali, Renee
#   Peers:
#   References:The graphics are by: @_toki_s
# ------------------------------------------------------
""" This Python script is for you to test your code before submitting it. 

Usage: click "Shell" next to "Console", then type "python3 tests.py" as shown below:
~/Final-Project$ python3 testsuite.py
"""
import unittest
from main import *
from buttons import *

class SimpleTest(unittest.TestCase):
  # def test_myTestedFunction(self):
      # self.assertEqual(myTestedFunction(True), "Happy")
      # self.assertEqual(myTestedFunction(False), "Sad") 
    
  ### Add you test cases here.
  def test_aestheticChoice(self):
    self.assertEqual(aestheticChoice("school"), "school outfit is printed to window") 
    self.assertEqual(aestheticChoice("gym"), "gym outfit is printed to window") 
    self.assertEqual(aestheticChoice("party"), "party outfit is printed to window") 
    
  def inside(self):
    self.assertEqual(inside(win, Point(350, 150), Point(375, 165)), ) 
    self.assertEqual(inside(win, Point(345, 350), Point(675, 321)), ) 
   
    










    



if __name__ == '__main__':  
  unittest.main()
