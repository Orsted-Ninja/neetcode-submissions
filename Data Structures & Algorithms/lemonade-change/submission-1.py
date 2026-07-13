from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Map to store: bill_value -> count_of_bills
        register = defaultdict(int)
        
        for bill in bills:
            if bill == 5:
                register[5] += 1
                
            elif bill == 10:
                if register[5] == 0: 
                    return False
                register[5] -= 1
                register[10] += 1
                
            elif bill == 20:
                # Greedy choice using the map
                if register[10] > 0 and register[5] > 0:
                    register[10] -= 1
                    register[5] -= 1
                elif register[5] >= 3:
                    register[5] -= 3
                else:
                    return False
                    
        return True