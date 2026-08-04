from collections import deque

class Solution:
    def zigZagTraversal(self, root):
        if root is None:
            return []

        q = deque([root])
        result = []
        left_to_right = True

        while q:
            level = deque()
            size = len(q)

            for _ in range(size):
                node = q.popleft()

                if left_to_right:
                    level.append(node.data)
                else:
                    level.appendleft(node.data)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.extend(level)
            left_to_right = not left_to_right

        return result