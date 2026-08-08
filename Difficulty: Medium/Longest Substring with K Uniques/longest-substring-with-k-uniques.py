class Solution:
    def longestKSubstr(self, s, k):
        
        f = {} # f is deictionary
        low = 0
        high = 0
        result = -1
        
        for high in range(len(s)): # s is given string
        
            f[s[high]] = f.get(s[high],0)+1 #.get() gives the value of each element stored in dictionary and + 1 increase its value
            
            while len(f)>k:
                
                f[s[low]]-=1
                
                if f[s[low]]==0: # if any element is 0 delete from dictionary
                    del f[s[low]]
                        
                low +=1
            
            if len(f)==k: # because we need exact k element
                length = high -low+1
                result = max(length,result)
        
        return result