def isStackSequence(nums):
    while len(nums)>0 :
        if nums[0] != min(nums) :
            for i in range(nums[0],min(nums)+1,-1) :
                if nums[0] == i :
                    nums.remove(nums[0])
                else :
                    return False
                    break
        else :
            nums.remove(nums[0])

    return True


def main():
    print(isStackSequence([2, 1, 4, 3]))  # True가 리턴되어야 합니다
    print(isStackSequence([3, 1, 2, 4]))  # False가 리턴되어야 합니다


if __name__ == "__main__":
    main()