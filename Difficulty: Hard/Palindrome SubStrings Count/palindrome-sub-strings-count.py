class Solution:
    def countPS(self, s):
        # code here
        self.count = 0

        for i in range(len(s)):
            self.count += self.pal(s, i, i)
            self.count += self.pal(s, i, i + 1)

        return self.count

    def pal(self, s, left, right):
        count = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 >= 2:
                count += 1

            left -= 1
            right += 1

        return count