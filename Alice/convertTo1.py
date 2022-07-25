# int형의 숫자 num이 주어졌을 때 해당 num을 한정된 연산을 이용해 최대한 적은 연산 횟수로 1을 만들어야 한다. 가장 적은 케이스의 횟수를 구하라.
# 할 수 있는 연산은 3으로 나누기, 2로 나누기, 1 빼기 총 세가지이다.

# 다른 사람 풀이 - 95points
# def convertTo1(num):
#     count = 0
#     while (num > 1):
#         if ((num - 1) % 3 == 0):
#             count += 1
#             num -= 1
#         elif ((num - 1 - 1) % 3 == 0):
#             count += 2
#             num -= 2
#         elif (num % 3 == 0):
#             num //= 3
#             count += 1
#         elif (num % 2 == 0):
#             num //= 2
#             count += 1
#         else:
#             num -= 1
#             count += 1
#     return count

def convertTo1(num):
    nums = [num+1 for i in range(num+1)]
    nums[1] = 0
    for i in range(2, num+1):
        if i%2==0:
            if nums[int(i/2)] + 1< nums[i]:
                nums[i] = nums[int(i/2)] + 1
        if i%3==0:
            if nums[int(i/3)] + 1 < nums[i]:
                nums[i] = nums[int(i/3)] + 1
        if nums[i-1] + 1 < nums[i]:
            nums[i] = nums[i-1] + 1
    return nums[num]

def main():
    print(convertTo1(10))

if __name__ == "__main__":
    main()

# 젇답 출력 과정
# [11, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11]
# [11, 0, 1, 11, 11, 11, 11, 11, 11, 11, 11]
# [11, 0, 1, 1, 11, 11, 11, 11, 11, 11, 11] 
# [11, 0, 1, 1, 2, 11, 11, 11, 11, 11, 11]  
# [11, 0, 1, 1, 2, 3, 11, 11, 11, 11, 11]   
# [11, 0, 1, 1, 2, 3, 2, 11, 11, 11, 11]    
# [11, 0, 1, 1, 2, 3, 2, 3, 11, 11, 11]     
# [11, 0, 1, 1, 2, 3, 2, 3, 3, 11, 11]      
# [11, 0, 1, 1, 2, 3, 2, 3, 3, 2, 11]       
# [11, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]        
# 3