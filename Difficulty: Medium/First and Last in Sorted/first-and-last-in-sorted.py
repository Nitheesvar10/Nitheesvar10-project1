class Solution:

    def lb(self, arr, x):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] >= x:
                self.lower = mid
                right = mid - 1
            else:
                left = mid + 1

    def ub(self, arr, x):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] > x:
                self.upper = mid
                right = mid - 1
            else:
                left = mid + 1

    def find(self, arr, x):
        self.lower = None
        self.upper = None

        self.lb(arr, x)
        self.ub(arr, x)

        # x is not present
        if self.lower is None or arr[self.lower] != x:
            return [-1, -1]

        first = self.lower

        # If there is no element > x, last occurrence is the last index
        if self.upper is None:
            last = len(arr) - 1
        else:
            last = self.upper - 1

        return [first, last]