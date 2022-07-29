# 90 points
# def removeDuplicate(nums):
#     results = []
#     for i in nums :
#         if i not in results :
#             results.append(i)
#     return results

def removeDuplicate(nums):
    return list(set(nums))

def main():
    print(removeDuplicate([1, 1, 2, 2, 2, 2, 5, 7, 7, 8])) # [1, 2, 5, 7, 8]을 리턴해야 합니다

if __name__ == "__main__":
    main()