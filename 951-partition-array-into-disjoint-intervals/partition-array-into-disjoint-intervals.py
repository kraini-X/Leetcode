class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)

        prefixMax = [0] * n
        suffixMin = [0] * n

        prefixMax[0] = nums[0]
        suffixMin[-1] = nums[-1]

        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], nums[i])

        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i + 1], nums[i])

        for i in range(n - 1):
            if prefixMax[i] <= suffixMin[i + 1]:
                return i + 1