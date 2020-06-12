"""
Given a string,determine if it is compreised of all unique characters. 
For example, the string 'abcde' has all unique characters and should return True. 
The string 'aabcde' contains duplicate characters and should return false.
"""
import unittest

def check_unique_characters(text):
    return len(set(text)) == len(text)

class Test(unittest.TestCase):
    
    def test(self, sol):
        self.assertEqual(check_unique_characters(''), True)
        self.assertEqual(check_unique_characters('goo'), False)
        self.assertEqual(check_unique_characters('godefr'), True)
        print("ALL TEST CASES PASSED")
        
t = Test()
t.test(check_unique_characters)