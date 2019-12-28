#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #g,s升序排序
        g.sort()
        s.sort()
        #初始化指针i、j指向g、s
        res = 0
        i = 0
        j = 0
        g_length = len(g)
        s_length = len(s)
        #对比g[i]和s[j]
        while i < g_length and j < s_length:
            #满足胃口，把饼干喂给小朋友
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            #不满足胃口就继续    
            else:
                j += 1
        return res            
# @lc code=end

