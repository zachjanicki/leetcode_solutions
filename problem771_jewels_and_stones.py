class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j_dict = {}
        s_dict = {}
        for char in S:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
                
        count = 0
        for char in J:
            if char in s_dict:
                count += s_dict[char]
        return count
