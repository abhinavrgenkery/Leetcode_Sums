nums1 = [1,2]
nums2 = [3,4]


merged = nums1 + nums2
merged.sort()
medianindex = len(merged) // 2
if len(merged) % 2 == 0:
    print(float(merged[medianindex - 1] + merged[medianindex]) / 2)
else:
    print(float(merged[medianindex]))