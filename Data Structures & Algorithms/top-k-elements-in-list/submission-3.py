class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = {}
        
        for num in nums:
            freq_counter[num] = freq_counter.get(num,0) + 1
        bucket = [[] for _ in range(len(nums)+1)]

        for n , f in freq_counter.items():
            bucket[f].append(n)

        result = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if(len(result)) == k:
                    return result
        return result
        # for i in range(k):
        #     maxFreq = 0
        #     maxNumber = 0
        #     for j in freq_counter:
        #         if freq_counter[j] > maxFreq:
        #             maxNumber = j
        #             maxFreq = freq_counter.get(j)
        #     result.append(maxNumber)
        #     freq_counter.pop(maxNumber)
        # return result
