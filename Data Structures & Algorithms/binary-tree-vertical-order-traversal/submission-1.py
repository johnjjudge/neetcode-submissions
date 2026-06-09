# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = {}
        queue = deque([(root, 0)])
        minCol = 0
        maxCol = 0

        while queue:
            node, col = queue.popleft()
            if col in cols:
                cols[col].append(node.val)
            else:
                cols[col] = [node.val]
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        result = []
        for key in range(minCol, maxCol + 1):
            result.append(cols[key])
        return result
        #return [cols[c] for c in range(minCol, maxCol + 1)]
        