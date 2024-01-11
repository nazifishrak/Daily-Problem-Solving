from math import inf
import unittest


def max_height(heights, s, e):
    if e == 0 or s == len(heights):
        return 0

    max_so_far = -inf
    for i in range(s,e,1):
        if heights[i] > max_so_far:
            max_so_far = heights[i]
    return max_so_far


def trap_rainwater(heights):
    """
    Calculate the total amount of trapped rainwater.

    Given an array of integers representing the elevation map of non-negative integers 
    where each bar's width is 1, this function computes the amount of rainwater that 
    can be trapped between the bars after raining.
    Parameters:
    heights (List[int]): A list of non-negative integers representing the elevation map.
                         Each element in the list indicates the height of a bar at that index.

    Returns:
    int: The total units of rainwater trapped.

    Example:
    >>> trap_rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    6

    Note:
    This function does not modify the input list.
    """

    total_water =0
    for p1 in range(len(heights)):
        curr_water = min(max_height(heights,0 ,p1), max_height(heights, p1+1, len(heights))) - heights[p1]
        if curr_water >0:
            total_water += curr_water
    
    return total_water


class Test(unittest.TestCase):
    def test_trap_rainwater(self):
        self.assertEqual(trap_rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(trap_rainwater([3,4,3]), 0)


if __name__ == '__main__':
    unittest.main()



