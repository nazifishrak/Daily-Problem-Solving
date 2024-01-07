def max_area(heights):
    """
    Calculates the maximum area of water that can be trapped between vertical lines in the given array.

    Args:
        heights (List[int]): An array of non-negative integers representing the heights of the vertical lines.

    Returns:
        int: The maximum area of water that can be trapped.

    Example:
        >>> max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
    """
    max_area = 0
    for p1 in range(len(heights)):
        for p2 in range(p1+1, len(heights)):
            l = min(heights[p1], heights[p2])
            w = p2 - p1 
            area = l*w
            max_area = max(max_area, area)
    
    return max_area
        


def max_area_optimied(heights):
    p1= 0
    p2 = len(heights)-1
    max_area =0

    while p1<p2:
        width = p2-p1
        height = min(heights[p1], heights[p2])
        area = width * height 
        max_area= max(area, max_area)
        if heights[p1] < heights[p2]:
            p1+=1
        else:
            p2-=1
    return max_area







        




    


import unittest

class findMaxAreaTestClass(unittest.TestCase):
    def test_max_area(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
    def test_max_area_optimised(self):
        self.assertEqual(max_area_optimied([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

if __name__ == "__main__":
    unittest.main()