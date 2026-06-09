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

        while queue:
            node, pos = queue.popleft()
            if node:
                if pos in cols:
                    cols[pos].append(node.val)
                else:
                    cols[pos] = [node.val]
                queue.append((node.left, pos - 1))
                queue.append((node.right, pos + 1))

        result = []
        for key in sorted(cols):
            result.append(cols[key])
        return result
        #return [cols[x] for x in sorted(cols)]
