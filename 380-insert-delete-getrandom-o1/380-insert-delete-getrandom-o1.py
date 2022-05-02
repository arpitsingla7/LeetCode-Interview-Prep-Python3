class RandomizedSet:

    def __init__(self):
        #maps num to ind in list
        self.hashMap = {}
        #stores all the elements of hashmap
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.hashMap
        if res:
            self.hashMap[val] = len(self.numList)
            self.numList.append(val)
            
        return res

    def remove(self, val: int) -> bool:
        res = val in self.hashMap
        
        if val in self.hashMap:
            #find ind of elem to be removed
            #switch values with last elem
            #remove last ele
            #del val from dict
            #update the ind of lastval
            
            indx = self.hashMap[val]
            lastVal = self.numList[-1]
            self.numList[indx] = lastVal
            self.hashMap[lastVal] = indx
            self.numList.pop()
            del self.hashMap[val]
        
        return res
            
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()