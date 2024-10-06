# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        di  = defaultdict(int)

        for num in arr:
            di [num %k] += 1

        print(di)

        
        for key , value in di.items():
            mod = -key % k
            if mod in di and di[mod] == value and mod + key == k:
                di[key] = 0
                di[mod] = 0
            elif key == 0:
                continue
            else:
                print("hi")
                return False
        print(di)
        if 0 in di and di[0] %2 != 0:
            return False
        
        return True