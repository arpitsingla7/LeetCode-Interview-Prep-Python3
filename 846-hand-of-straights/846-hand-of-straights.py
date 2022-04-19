class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        
        hashMap = {}
        for i in hand:
            hashMap[i] = 1 + hashMap.get(i, 0)
            
        hand.sort()
        
        #get min ele from arr
        # search nxt in hashMap
        # - from hashMap
        #edge cases: if not their return false
        
        
        while hand:
            
            first = hand.pop(0)
            
            for nxt in range(groupSize-1):
                if first+1 not in hashMap:
                    return False
                
                hashMap[first+1]-=1
                if hashMap[first+1]==0:
                    del hashMap[first+1]
                
                hand.remove(first+1)
                first = first+1
        return True
                
                    
                    
            