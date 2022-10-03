class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #declaring a hashmap
        rhashmap={0:1}
        
        #initialize count  and rsum as zero
        count=0
        rSum=0
        
        #iterating through the length of array
        for i in range(len(nums)):
            #counting the rsum value 
            rSum+=nums[i]
            #declare a variable which contains running sum minus target
            compliment= rSum-k

            
            #if the compliment value in hashmap
            if compliment in rhashmap:
                #increment the value to the hashmap
                count+=rhashmap[compliment]
            
            #if running sum is in the hashmap just increment it by 1
            if rSum in rhashmap:
                rhashmap[rSum]+=1
                
            #if running sum is encountered first then initialize it to 1    
            else:
                 rhashmap[rSum]=1
                
         #finally return the counted value       
        return count       
                