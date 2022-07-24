# 0점..ㅜ
# def moveZerosToEnd(nums):
#     for i in nums :
#         if i == 0 :
#             nums.remove(0)
#             nums.append(0)
#     return nums

# 0점..
# def moveZerosToEnd(nums):
#     zero_num = nums.count(0)
#     for i in range(zero_num) :
#         nums.remove(0)
#         nums.append(0)
#     return nums
#

def moveZerosToEnd(nums) :
    currentPosition = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums.insert(currentPosition, nums.pop(i))
            currentPosition += 1
    return nums

# def moveZerosToEnd(nums) :
#     currentPosition = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[currentPosition] = nums[i]
#             if i != currentPosition:
#                 nums[i] = 0
#             currentPosition += 1
#     return nums

def main():
    print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))

if __name__ == "__main__":
    main()
