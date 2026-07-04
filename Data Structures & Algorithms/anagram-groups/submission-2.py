class Solution:
    @staticmethod
    def calculateKey(s:str)-> tuple[int,...]:
        s = s.lower()

        alpha_frequency_counter = [0] * 26
        for i in range(len(s)):
            pos = ord(s[i]) - ord('a')
            if 0 <= pos < 26:
                alpha_frequency_counter[pos]+=1
        
        return tuple(alpha_frequency_counter)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for i in range(len(strs)):
            key = self.calculateKey(strs[i])
            seen[key].append(strs[i])
        return list(seen.values())



        