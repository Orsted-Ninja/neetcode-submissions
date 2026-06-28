class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s=0
        l=0
        people.sort()
        r=len(people)-1
        while l<=r:
            if abs(people[l]+people[r])<=limit :
                 l+=1
                
            s+=1
            r-=1
        return s
        
            
            

        