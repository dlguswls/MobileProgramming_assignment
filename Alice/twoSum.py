# 첫 시도 - 90 points
# def twoSum(nums, target) : 
#     num1, num2 = '', ''
#     for i in range(len(nums)) : 
#         for k in range(i+1, len(nums)): 
#             if (nums[i] + nums[k]) == target : 
#                 num1 = nums[i]
#                 num2 = nums[k]
#                 break
#         if num1 != '' : 
#             break
#     return num1, num2

def twoSum(nums, target) : 
    nums.sort()
    num1 = 0
    num2 = len(nums) - 1
    while num1 < num2 : 
        sum = nums[num1] + nums[num2]
        if sum == target : 
            return nums[num1], nums[num2]
        elif sum > target : 
            num2 -= 1
        else : 
            num1 += 1

def main() : 
    print(twoSum([2, 8, 19, 37, 4, 5], 12))  # 4 혹은 8 리턴

if __name__ == "__main__" : 
    main()
