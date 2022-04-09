class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        l, r = 0, len(nums)-1
        
        while l<=r:
            
            #array is sorted
            if nums[l]<nums[r]:
                #run binary search
                while l<=r:
                    print("in")
                    m = l+(r-l)//2
                
                    if target==nums[m]:
                        return m
                    elif target>nums[m]:
                        l=m+1

                    elif target<nums[m]:
                        r = m-1
                
                return -1
            
            else:
                
                m = l+(r-l)//2
                if target==nums[m]:
                    return m

                if nums[l]<=nums[m]:
                    if target<nums[l] or target>nums[m]:
                        l=m+1
                    else:
                        r=m-1
                
                else:
                    if target>nums[r] or target<nums[m]:
                        r = m-1
                    
                    else:
                        l = m+1 
        
        return -1