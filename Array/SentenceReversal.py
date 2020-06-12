"""
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading 
and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'
"""

import unittest

def reverse_word(text):
    text = text.strip().split()
    result = ""
    for i in range(len(text) - 1, -1, -1):
        result += text[i] + " "
    return result[:-1]

    # return " ".join(reversed(text.split()))

class Test(unittest.TestCase):
    def test(self, sol):
        self.assertEqual(sol('    space before'),'before space')
        self.assertEqual(sol('space after     '),'after space')
        self.assertEqual(sol('   Hello John    how are you   '),'you are how John Hello')
        self.assertEqual(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
t = Test()
t.test(reverse_word)