class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        f = {} # empty dictionary to store fruit numbers
        low  = 0
        high = 0
        result = -1 # initialise

        for high in range(len(fruits)):
            f[fruits[high]]=f.get(fruits[high],0) + 1 # .get() helps to find value of each fruit and +1 increase it 

            while len(f) > 2: # here basket is 2
                f[fruits[low]] -=1

                if f[fruits[low]]==0: # if any fruit's value is 0 then delete from dictionary
                    del f[fruits[low]]
                low +=1

            length = high -low +1
            result = max(length,result)

        return result