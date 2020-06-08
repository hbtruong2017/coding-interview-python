"""
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

 """

def pair_sum(arr, k):
    counter = 0
    lookup = set()

    for num in arr:
        if k - num in lookup:
            counter += 1
        else:
            lookup.add(num)
            
    return counter


import unittest

class TestPair(unittest.TestCase):
    
    def test(self,sol):
        self.assertEqual(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        self.assertEqual(sol([1,2,3,1],3),1)
        self.assertEqual(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)
    