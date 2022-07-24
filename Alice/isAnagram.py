def isAnagram(str1, str2):
    for i in str1 :
        if i not in str2 :
            return False
    return True


def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle'))  # should return True
    print(isAnagram('cat', 'cap'))  # should return False


if __name__ == "__main__":
    main()