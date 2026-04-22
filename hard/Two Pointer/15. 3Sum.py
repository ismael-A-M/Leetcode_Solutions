class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr = sorted(nums)
        res = []
        n = len(arr)

        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            val = -arr[i]
            left, right = i + 1, n - 1

            while left < right:
                s = arr[left] + arr[right]

                if s == val:
                    res.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

                elif s > val:
                    right -= 1
                else:
                    left += 1

        return res