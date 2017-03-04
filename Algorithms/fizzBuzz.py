class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        for i in range(1, n+1):
            
            if (i % 15 == 0):
                results.append("FizzBuzz")
                
            elif (i % 3 == 0):
                results.append("Fizz")
            
            elif (i % 5 == 0):
                results.append("Buzz")
            
            else:
                results.append(str(i))
                
        return results