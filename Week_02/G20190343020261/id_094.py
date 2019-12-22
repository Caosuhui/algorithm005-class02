#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
    #WHITE 未访问的新节点；GRAY 已访问的节点
        WHITE , GRAY = 0 , 1
    #设置根节点默认为未访问
        res = []
        stack = [{WHITE, root}]
    #若根节点，依次根据左节点、根节点、右节点出栈
        while stack:
            color, node = stack.pop()
            if node is None: continue
            #当前指向的节点是未访问过的节点，依次左节点、根节点、右节点入栈
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res    
# @lc code=end

    

