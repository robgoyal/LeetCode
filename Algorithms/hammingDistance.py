class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        diff = 0

        # Format x,y as 32 bit numbers left padded with zeroes
        x_bin = '{0:032b}'.format(x)
        y_bin = '{0:032b}'.format(y)

        # Difference check
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                diff += 1
        
        return diff