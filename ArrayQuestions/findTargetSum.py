#Find two numbers in an array that sum up to the target number
#[7, 2, 3, 5, 100]

def find_target_sum(arr, tar):
    """
    This function finds the first pair of numbers in the array that add up to the target sum.
    It uses a nested loop to iterate over the array, which results in a time complexity of O(n^2).
    If no such pair exists, it returns None.
    """
    for p1 in range(0, len(arr),1):
        num_to_find = tar- arr[p1]
        for p2 in range(p1+1, len(arr),1):
            if arr[p2] == num_to_find:
                return [p1, p2]
    return None


def optimised_sol(arr, tar):
    """
    This function is an optimized solution for finding two numbers in an array that add up to a target sum.
    It uses a dictionary to store the numbers it needs to find to reach the target sum and their indices.
    It iterates over the array once, checking for each number if its complement to reach the target sum is in the dictionary.
    If it is, it returns the indices of the two numbers. If it's not, it adds the complement of the current number to the dictionary.
    If it goes through the entire array without finding a pair that adds up to the target, it returns None.
    """
    lookup_table = {}
    for p1 in range(0, len(arr),1):
        ntf = tar - arr[p1]
        if arr[p1] in lookup_table:
            return [lookup_table[arr[p1]], p1]
        else:
            lookup_table[ntf]=p1
    return None


import unittest

class TestClass(unittest.TestCase):
    def test_find_target_sum(self):
        self.assertEqual(find_target_sum([7, 2, 3, 5, 100], 8), [2,3])
        self.assertEqual(find_target_sum([], 8), None)
        self.assertEqual(find_target_sum([7, 2, 3, 5, 100], 200), None)

    def test_optimised_sol(self):
        self.assertEqual(optimised_sol([7, 2, 3, 5, 100], 8), [2,3])
        self.assertEqual(optimised_sol([], 8), None)
        self.assertEqual(optimised_sol([7, 2, 3, 5, 100], 200), None)



if __name__== '__main__':
    unittest.main()









