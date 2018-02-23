class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        This is too slow in python to pass all the test cases
        s_as_list = list(s)
        new_s = ''
        for i in range(len(s_as_list)):
            new_s += s_as_list.pop()
        return new_s
        '''
        
        s_as_list = list(s)
        for i in range(len(s) / 2):
            s_as_list[i], s_as_list[-i -1] = s_as_list[-i - 1], s_as_list[i]
        return ''.join(s_as_list)
