class Solution:
    def containsNearbyAlmostDuplicate(
        self,
        nums: List[int],
        indexDiff: int,
        valueDiff: int
    ) -> bool:

        bucket = {}
        width = valueDiff + 1

        for i, num in enumerate(nums):

            bucket_id = num // width

            
            if bucket_id in bucket:
                return True

            if bucket_id - 1 in bucket:
                if abs(num - bucket[bucket_id - 1]) <= valueDiff:
                    return True


            if bucket_id + 1 in bucket:
                if abs(num - bucket[bucket_id + 1]) <= valueDiff:
                    return True

            bucket[bucket_id] = num


            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // width
                del bucket[old_bucket]

        return False