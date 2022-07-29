def findDifference(str1, str2):
    a = list(str1)
    b = list(str2)
    for i in a :
        b.remove(i)
    return b[0]


def main():
    print(findDifference("apple", "azlppe"))


if __name__ == "__main__":
    main()