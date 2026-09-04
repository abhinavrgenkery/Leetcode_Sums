known = {}
nums=[2, 7, 11, 15]
target = 9
for i in range(len(nums)):
    req = target - nums[i]

    if req in known:
        print([known[req], i])

    known[nums[i]] = i
