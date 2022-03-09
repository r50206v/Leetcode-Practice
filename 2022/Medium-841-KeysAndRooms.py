class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set([0])
        queue = [rooms[0]]
        
        while queue: 
            
            node = queue.pop(0)
            for next_node in node:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(rooms[next_node])
        
        return len(visited) == len(rooms)