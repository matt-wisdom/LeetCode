class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)  
        idx = sorted(range(len(nums)), key=lambda k: nums[k])
        nums_sorted = [nums[i] for i in idx]
        tm = round(target/2)+1
        for i in range(n): 
            num1 = nums_sorted[i]
            if num1 > (tm):
                break
            try:
                i1 = idx[i]
                nums[i1] = 10**10
            except ValueError:
                continue
            try:
                i2 = nums.index(target-num1)
                nums[i2] = 10**10
            except ValueError:
                continue
