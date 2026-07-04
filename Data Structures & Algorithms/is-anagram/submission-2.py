class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_counter = [0] * 26
        s = s.lower()
        t = t.lower()
        for i in range(len(s)):
            char_index = ord(s[i]) - ord('a')
            alpha_counter[char_index]+=1
        for i in range(len(t)):
            char_index = ord(t[i]) - ord('a')
            alpha_counter[char_index]-=1
        
        for i in range(len(alpha_counter)):
            if(alpha_counter[i]!=0):
                return False
        return True
    
    # def isAnagram(self, s: str, t: str) -> bool:
    # return sorted(s) == sorted(t)

    # def isAnagram(self, s: str, t: str) -> bool:
    #     return Counter(s.lower()) == Counter(t.lower())