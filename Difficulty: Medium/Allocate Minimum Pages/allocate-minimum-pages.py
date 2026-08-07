class Solution:
    def findPages(self, arr, k):
        # If students are more than books, allocation is impossible
        if k > len(arr):
            return -1

        low = max(arr)
        high = sum(arr)
        ans = -1

        while low <= high:
            allot = low + (high - low) // 2

            if self.ok(arr, k, allot):
                ans = allot
                high = allot - 1
            else:
                low = allot + 1

        return ans

    def ok(self, arr, k, allot):
        count = 1
        cur_page_count = 0

        for pages in arr:
            if cur_page_count + pages > allot:
                count += 1
                cur_page_count = pages
            else:
                cur_page_count += pages

        return count <= k