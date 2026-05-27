class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = deque([node])
        # seen maps: original_node -> cloned_node
        seen = {node: Node(node.val)}
        
        while len(queue) > 0:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in seen:
                    seen[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # Add the cloned neighbor to the current cloned node's neighbors list
                seen[curr].neighbors.append(seen[neighbor])

        return seen[node]