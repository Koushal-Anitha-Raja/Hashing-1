class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #initializting the hashmap
        hashmap={}
        #creating a hashset
        seen=set()

        #iterating through the string
        for i in range(len(s)):
            
            #if new element is added to hashmap 
            if s[i]not in hashmap:
                #if the value is already seen the return false
                if t[i] in seen:
                    return False
                #then map s with the t element
                hashmap[s[i]]=t[i]
                #adding t of i values  to hashset if it is first encountered
                seen.add(t[i])
                
                
            #if it is already there then 
            else:
                if hashmap[s[i]]!=t[i]:
                    return False
        return True     
            
        