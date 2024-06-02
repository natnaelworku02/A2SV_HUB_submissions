# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        arr= s.split()
        
        arr.sort(key= lambda x : int(x[-1]))
        for i in range(len(arr)):
            arr[i]= arr[i][:-1]

        return ' '.join(arr)
        


        