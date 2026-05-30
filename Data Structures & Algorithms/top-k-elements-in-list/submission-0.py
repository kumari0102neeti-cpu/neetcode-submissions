class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countnums  = {}
        for i in nums:
            countnums[i] = countnums.get(i, 0) + 1

        sortedDict = dict(sorted(countnums.items() , key = lambda item:item[1], reverse = True))
        print(sortedDict)
        c , result = 0, []
        for i in sortedDict.keys():
            if (c < k):
                result.append(i)
            c += 1
        
        return result
            

        
        