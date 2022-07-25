# 첫 시도 - 80 points
# def maxTwoDiff(nums):
#     nums.sort()
#     return nums[-1]-nums[0]

def maxTwoDiff(nums):
    result = max(nums) - min(nums)
    return result
    
def main():
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # 49가 리턴되어야 합니다.

if __name__ == "__main__":
    main()
