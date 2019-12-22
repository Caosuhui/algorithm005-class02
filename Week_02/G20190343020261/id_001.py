#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #定义hashmap
        hashmap = {}
        #循环如果target-num 值存在，就返回对应下标
        for i,num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [hashmap.get(target - num), i]
            #去重复值
            hashmap[num] = i
# @lc code=end

