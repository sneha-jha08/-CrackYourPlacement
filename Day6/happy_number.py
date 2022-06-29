class Solution:
    
    def isHappy(self, n: int) -> bool:
        
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum
        
        while n != 1 and n != 4:
            n = get_next(n)
            
        return n == 1
      
      ##recursion, make diff func for next num, curr_sum= sum of square of digit , curr_sum will be returned, till n!=1 and 4 we will recurr the func. and return n==1
