class Solution:
    def minWindow(self, s: str, t: str) -> str:

        needed = {}
        have = {}

        # Create needed hashmap
        for ch in t:
            needed[ch] = needed.get(ch, 0) + 1

        low = 0
        res = float('inf')
        start = 0

        for high in range(len(s)):

            # Add current character
            have[s[high]] = have.get(s[high], 0) + 1

            # Check if current window is valid
            while self.correct(have, needed):

                length = high - low + 1

                if length < res:
                    res = length
                    start = low

                # Remove left character
                have[s[low]] -= 1
                low += 1

        if res == float('inf'):
            return ""

        return s[start:start + res]

    #For every character I need, if my window doesn't have enough of it, return False. If I checked everything and nothing was missing, return True
    def correct(self, have, needed):

        for ch in needed:
            if have.get(ch, 0) < needed[ch]:
                return False

        return True