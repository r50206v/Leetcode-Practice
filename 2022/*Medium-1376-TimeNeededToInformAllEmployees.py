class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        
		#construct employee tree
        empTree = defaultdict(list)
        for i, emp in enumerate(manager):
            if emp == -1 : continue
            empTree[emp].append(i)
        
        if len(empTree) == 0 : return 0
        
		#start dfs
        return self.dfs_max(headID, empTree, informTime, 0)
        
    
    def dfs_max(self, node, empTree, informTime, time):
        if empTree[node] == [] :
            return time
        
        resTime = 0
        for subordinate in empTree[node]:
            resTime = max(resTime, self.dfs_max(subordinate, empTree, informTime, time + informTime[node])) 
        return resTime