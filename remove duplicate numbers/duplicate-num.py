class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        j = 1
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                continue
            a[j] = a[i+1]
            j+=1
        return j