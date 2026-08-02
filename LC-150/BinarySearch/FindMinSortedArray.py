class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minimum = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                minimum = min(minimum, nums[left])

            mid = (left + right) // 2
            minimum = min(minimum, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minimum
        



