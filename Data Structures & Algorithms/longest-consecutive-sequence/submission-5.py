class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        loopup_set = set()
        for num in nums:
            loopup_set.add(num)
        
        longest_consecutive = 1
        for n in loopup_set:
            if n - 1  not in loopup_set:
                maxCount = 1
                current_num = n 
                while current_num + 1 in loopup_set:
                    maxCount+=1
                    current_num+=1
                longest_consecutive = max(longest_consecutive,maxCount)
        return longest_consecutive
                
