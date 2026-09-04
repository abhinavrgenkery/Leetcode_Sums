nums=[1,2,1]
catenated = [0] * 2 * len(nums)
for i in range(len(nums)):
    catenated[i] = nums[i]
for i in range(len(nums)):
    catenated[len(nums)+i] = nums[i]
print(catenated)