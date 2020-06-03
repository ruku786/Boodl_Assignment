# Problem 1 :- Sum to N

class Solution:
    def Sum(self, nums, target):
        look = {}
        for n, x in enumerate(nums):
            try:
                return(look[x], n)
            except KeyError:
                look.setdefault(target - x, n)

test= Solution()
a1 = [1, 3, 5]
a2 = [2, 5, 6]
given_num = [2, 7, 11, 15]
print(test.Sum(a1, 4))
print(test.Sum(a2, 7))
print(test.Sum(given_num, 9))