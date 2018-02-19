class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        output_list = []
        for num in range(left, right + 1):
            num_as_str = str(num)
            is_valid = True
            for number in num_as_str:
                if number == '0' or num % int(number) or is_valid == False:
                    is_valid = False
            if is_valid:
                output_list.append(num)
        return output_list
