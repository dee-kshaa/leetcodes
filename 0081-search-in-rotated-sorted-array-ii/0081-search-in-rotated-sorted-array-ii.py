class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        size: int = len(arr)

        # i need to rm duplicates
        nums: list[int] = []
        i: int = 0
        while i < size-1:
            if arr[i] != arr[i+1]:
                nums.append(arr[i])
            i += 1

        nums.append(arr[size-1])

        start: int = 0
        end: int = len(nums) - 1

        while start <= end:
            mid: int = start + (end - start) // 2

            if nums[mid] == target:
                return True

            if nums[start] <= nums[mid]:
                # this part is sorted
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # means this part is sorted
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return False