class Solution:
    def aggressiveCows(self, arr, k):
        arr.sort()

        low = 1
        high = arr[-1] - arr[0]
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2

            if self.largmin(arr, k, mid):
                ans = mid
                low = mid + 1      # Try for a larger minimum distance
            else:
                high = mid - 1     # Reduce the distance

        return ans

    def largmin(self, arr, k, dis):
        co_ord = arr[0]
        cnt = 1

        for i in range(1, len(arr)):
            if arr[i] - co_ord >= dis:
                cnt += 1
                co_ord = arr[i]

                if cnt == k:
                    return True

        return False