"""
Given a string of opening and closing parentheses, check whether it’s balanced. 
We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. 
Assume that the string doesn’t contain any other character than these, no spaces words or numbers. 
As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. 
For example ‘([])’ is balanced but ‘([)]’ is not.

You can assume the input string has no spaces.
"""

import unittest

def balance_check(text):

    if len(text) % 2 != 0:
        return False

    opening_brac = ["{", "(", "["]
    dict_brac = {"{":"}", "(":")", "[":"]"}
    temp = []

    for char in text:
        if char in opening_brac:
            temp.append(char)
        elif char != dict_brac[temp.pop()]:
            return False

    if len(temp) > 0:
        return False

    return True

class Test(unittest.TestCase):

    def test(self, sol):
        self.assertEqual(sol('[](){([[[]]])}('),False)
        self.assertEqual(sol('[{{{(())}}}]((()))'),True)
        self.assertEqual(sol('[[[]])]'),False)
        self.assertEqual(sol('([])'), True)
        self.assertEqual(sol('([)]'), False)
        print('ALL TEST CASES PASSED')

t = Test()
t.test(balance_check)
