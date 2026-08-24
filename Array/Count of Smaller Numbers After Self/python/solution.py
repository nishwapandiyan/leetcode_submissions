class Solution:
    def countSmaller(self, nums):
        n = len(nums)

        arr = [(nums[i], i) for i in range(n)]
        ans = [0] * n

        def mergeSort(arr):

            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            merged = []

            i = 0
            j = 0

            while i < len(left) and j < len(right):

                if left[i][0] <= right[j][0]:
                    ans[left[i][1]] += j
                    merged.append(left[i])
                    i += 1

                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                ans[left[i][1]] += j
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        mergeSort(arr)

        return ans