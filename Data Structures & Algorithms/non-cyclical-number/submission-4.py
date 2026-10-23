class Solution:
    def isHappy(self, n: int) -> bool:
        
        arr = []
        def extract_last_digit(number):
            return number % 10
        
        from collections import defaultdict
        seen = defaultdict(int)

        while True:
            while n > 0:
                arr.append(int(extract_last_digit(n)**2))
                n //= 10
            
            if sum(arr) in seen:
                return False
            elif sum(arr) == 1:
                return True
                
            seen[sum(arr)] = 0
            n = sum(arr)

            arr = []
        
        return int(sum(arr)) == 1