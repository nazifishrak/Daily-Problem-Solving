"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

"""

def compare(a,b):
    # "a#z". "aba##z"
    arr_a=[]
    arr_b =[]
    for i in a:
        if i =="#":
            if arr_a !=[]:
                arr_a.pop()
        else:
            arr_a.append(i)
            
    for i in b:
        if i =="#":
            if arr_b !=[]:
                arr_b.pop()
        else:
            arr_b.append(i)
            
    return arr_a == arr_b
    
# print(compare("a#z", "ab##z"))


import unittest

class TestClass(unittest.TestCase):
    def test_compare(self):
        self.assertEqual(compare("a#z", "ab##z"), True)
        



if __name__== '__main__':
    unittest.main()