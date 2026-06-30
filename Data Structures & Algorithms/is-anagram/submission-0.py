class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Use an array to store frequency of each letter (26 lowercase English letters)
        count = [0] * 26
        
        for i in range(len(s)):
            # Increment for string s and decrement for string t
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            
        # If strings are anagrams, all counts must return to zero
        for val in count:
            if val != 0:
                return False
                
        return True
        