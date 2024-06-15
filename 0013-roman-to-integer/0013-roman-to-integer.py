class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
# Not that optimised, later I realised that I dont need to have all these checks
        i = 0
        num = 0
        while i < len(s):
            if i + 1 < len(s):
                if (s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X")):
                    num += dic[s[i + 1]] - dic[s[i]]
                    i += 2
                elif (s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C")):
                    num += dic[s[i + 1]] - dic[s[i]]
                    i += 2
                elif (s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M")):
                    num += dic[s[i + 1]] - dic[s[i]]
                    i += 2
                else:
                    num += dic[s[i]]
                    i += 1
            else:
                num += dic[s[i]]
                i += 1

        return num
