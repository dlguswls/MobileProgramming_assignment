# 첫 시도 - 90 points
# def findDuplicate(nums):
#     set_nums = list(set(nums))
#     for i in set_nums : 
#         nums.remove(i)
#     return nums[0]

# 두 번째 시도 - 90 points
# def findDuplicate(nums):
#     set_nums = []
#     dup = [x for x in nums if x in set_nums or set_nums.append(x)]
#     return dup[0]

# 세 번째 시도 - 90 points
# def findDuplicate(nums):
#     dup = [x for i, x in enumerate(nums) if x in nums[:i]]
#     return dup[0]

def findDuplicate(nums):
    set_nums = set()
    for i in nums:
        if i in set_nums:
            return i
        else:
            set_nums.add(i)

def main():
    print(findDuplicate([1, 5, 2, 4, 5, 6, 3]))

if __name__ == "__main__":
    main()