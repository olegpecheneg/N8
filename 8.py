def kbig(nums, k):

    def maxi(nums):
        
        maxx = 0
        
        for i in nums:
            for j in nums:
                if j > maxx:
                    maxx = i
                else:
                    continue     
        return maxx
    
    def recur(nums, k):

        if k == 0:
            return maxi(nums)
        
        else:
            k -= 1
            nums.remove(maxi(nums))
            return recur(nums, k) 
        
    return recur(nums, k - 1)