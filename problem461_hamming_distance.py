class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_binary = self.convert_to_bin(x)
        y_binary = self.convert_to_bin(y)
        diff_count = 0
        for i in range(len(x_binary)):
            if x_binary[i] != y_binary[i]:
                diff_count += 1
        return diff_count
    
    def convert_to_bin(self, num):
        bin_list = []
        while num > 0:
            if num % 2:
                bin_list.append(1)
            else:
                bin_list.append(0)
            num /= 2
        slots_remaining = 32 - len(bin_list)
        for i in range(slots_remaining):
            bin_list.append(0)
        return bin_list
