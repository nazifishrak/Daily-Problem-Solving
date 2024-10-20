class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        index =[]
        for i,c in enumerate(s):
            if c.lower() in set(('a','e','i','o','u')):
                index.append(i)
        sp=0
        lp=len(index)-1
        s_list = list(s)
        while sp<lp:
            temp = s_list[index[sp]]
            s_list[index[sp]]=s_list[index[lp]]
            s_list[index[lp]]=temp
            sp+=1
            lp-=1
        return "".join(s_list)

        

        