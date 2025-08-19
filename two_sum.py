class Solution(object):
    def twoSum (self, nums, target):
        temp = []
        j = 0
        i = 1

        while j < len(nums):

            if i == len(nums):
                j += 1
                i = j+1

            if nums[j] + nums[i] == target:
                print(nums.index(nums[j]),nums.index(nums[i]))
                temp.append(j)
                temp.append(i)
                return temp
                break

            i += 1