# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        
        di = defaultdict(int)

        count = Counter(word)
        count = count.most_common()

        # print(count)
        

        num = 1

        items = 0
        ans = 0

        for key,val in count:
            
            ans += val*num
            items += 1

            if items == 8:
                items = 0
                num += 1
        
        return ans
