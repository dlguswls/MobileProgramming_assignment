## 이거 못 푼 문제ㅠ
def maxSubArray(nums):
    sum = 0
    max = 0
    for i in nums:
        sum += i
        if sum < 0:
            sum = 0
        if max < sum:
            max = sum
    return max

def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1])) # 30이 리턴되어야 합니다

if __name__ == "__main__":
    main()