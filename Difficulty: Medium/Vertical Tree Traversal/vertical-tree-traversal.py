class Solution:
    def verticalOrder(self, root):
        nodes = []
        cnt = 0

        def dfs(node, row, col):
            nonlocal cnt
            if node is None:
                return

            nodes.append((col, row, cnt, node.data))
            cnt += 1

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        nodes.sort(key=lambda x: (x[0], x[1], x[2]))

        ans = []
        prevcol = float("-inf")

        for col, row, order, val in nodes:
            if col != prevcol:
                ans.append([])
                prevcol = col
            ans[-1].append(val)

        return ans