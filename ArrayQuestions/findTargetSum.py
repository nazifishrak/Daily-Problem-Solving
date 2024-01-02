#Find two numbers in an array that sum up to the target number
#[7, 2, 3, 5, 100]

def find_target_sum(arr, tar):
    for p1 in range(0, len(arr),1):
        num_to_find = tar- arr[p1]
        for p2 in range(p1+1, len(arr),1):
            if arr[p2] == num_to_find:
                return [p1, p2]
    return None


import unittest

class TestClass(unittest.TestCase):
    def test_find_target_sum(self):
        self.assertEqual(find_target_sum([7, 2, 3, 5, 100], 8), [2,3])
        self.assertEqual(find_target_sum([], 8), None)
        self.assertEqual(find_target_sum([7, 2, 3, 5, 100], 200), None)


if __name__== '__main__':
    unittest.main()









