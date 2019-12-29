#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #初始化一个队列
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])    
        #定义岛屿的四个相邻位置
        q = list()
        res = 0
        area = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        #遍历
        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
            #遍历过程中发现了岛屿
                if cur == '1':
                    # 陆地数量+1
                    res += 1
                    #入队列
                    q.append((i, j))
                    #将岛屿沉没即置为0
                    grid[i][j] = '0'
        #如果队列不为空，就循环队列，将队列里已经存在的岛屿进行BFS
                while len(q) > 0:
                    #取出岛屿坐标
                    node_x, node_y = q[0]
                    del q[0]
                    #判断岛屿的四个相邻位置是否存在还存在岛屿
                    for k in range(len(area)):
                        area_x, area_y = area[k]
                        node_area_x, node_area_y = node_x + area_x, node_y + area_y
                        if (node_area_x >= 0 and node_area_x < m) and (node_area_y >= 0 and node_area_y < n):
                            if grid[node_area_x][node_area_y] == '1':
                                # 相邻位置存在岛屿：入队列、把岛屿沉没
                                q.append((node_area_x, node_area_y))
                                grid[node_area_x][node_area_y] = '0'
        return res                
        
# @lc code=end

