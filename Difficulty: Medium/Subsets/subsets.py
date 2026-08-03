class Solution:
    def solve(self, idx, subset, arr):
        if idx == len(arr):
            self.result.append(subset.copy())
            return

        subset.append(arr[idx])
        self.solve(idx + 1, subset, arr)

        subset.pop()
        self.solve(idx + 1, subset, arr)

    def subsets(self, arr):
        self.result = []
        subset = []

        self.solve(0, subset, arr)
        return self.result