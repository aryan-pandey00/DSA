class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        high = 0
        result = 0
        f = {} # dictionary to store value

        for high in range(len(s)):
            f[s[high]] = f.get(s[high],0) + 1 #.get() helps to fetch value of each character

            k = high -low +1 # size of window 
            
            # check for duplicate
            while len(f) <k:  # Number of unique characters < size of window → therefore there is a duplicate
                f[s[low]] -=1

                if f[s[low]] == 0:
                    del f[s[low]]

                low +=1
                k = high -low +1 # when low change the value of k also change 

            length = k # here k = high-low +1
            result = max(length,result)

        return result