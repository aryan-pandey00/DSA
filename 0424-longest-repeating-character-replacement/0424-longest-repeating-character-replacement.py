class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = 0
        high = 0 
        result = 0
        a = {}  # dict to store characters frequency
        
        for high in range(len(s)):
            a[s[high]] = a.get(s[high],0) + 1 # add charcter

            length = high-low + 1
            max_count = max(a.values()) # find highest frequensy character
            diff = length - max_count # find charcter neeed to replace

            while diff > k: # replacement more than k then shrink window
                a[s[low]] -=1

                if a[s[low]] == 0: # if character becomes 0 delete it
                    del a[s[low]]

                low +=1
                
                # update 
                max_count = max(a.values())
                length = high -low + 1
                diff = length - max_count

            if diff < k or diff == k:
                length = high - low +1
                result = max(length,result)

        return result