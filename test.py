def doManythings(nums) :
	allPairs = []   # 1회
	for i in range(len(nums)) :
		for j in range(len(nums)) :   # N*N회
			## 두 번째 for문 안에서 조건문 1회, 그 안의 append 1회 -> 2회
			if nums[i] < nums[j] :
				allPairs.append((nums[i], nums[j]))
			else :
				allPairs.append((nums[i], nums[j]))
	return allPairs
print(doManythings([3,4,6,1,4,7,8,2]))