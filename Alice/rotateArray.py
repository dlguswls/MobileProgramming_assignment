# partialReverse 함수 사용하지 않을 때
# def rotateArray(nums, k):
#     index = (len(nums)-k)
#     return nums[index:] + nums[:index]

# partialReverse 함수 사용할 때
# partialReverse(nums, 0, len(nums)-1) => [9, 8, 7, 6, 5, 4, 3, 2, 1]
# 이 때 [9, 8, 7, 6], [5, 4, 3, 2, 1]을 한번씩 더 회전해주면 됨
def rotateArray(nums, k):
    partialReverse(nums, 0, len(nums)-1)
    partialReverse(nums, 0, k-1)
    partialReverse(nums, k, len(nums)-1)
    return nums


# 다음 함수는 추가적인 공간 사용 없이 배열의 일부를 뒤집어 주는 함수입니다.
# 예를 들어, nums = [1,2,3,4,5]
# partialReverse(nums, 1, 3)
# 을 실행 할 경우, nums = [1, 4, 3, 2, 5] 가 됩니다.
# 필요하다면 사용하세요.
def partialReverse(nums, start, end):
    for i in range(0, int((end - start) / 2) + 1):
        temp = nums[start + i]
        nums[start + i] = nums[end - i]
        nums[end - i] = temp

def main():
    nums = [1, 2, 3, 4, 5]
    partialReverse(nums, 1, 3)  # [1, 4, 3, 2, 5] 를 반환합니다.
    print(nums)
    print(rotateArray([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))  # [6,7,8,9,1,2,3,4,5] 를 반환해야 합니다.

if __name__ == "__main__":
    main()
