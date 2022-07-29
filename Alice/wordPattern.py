def wordPattern(pattern, strList):
    pattern_set = list(set(pattern))
    strList_set = []
    for i in pattern_set:
        strList_set.append(strList[pattern.index(i)])
    for i in range(len(strList)):
        if strList[i] != strList_set[pattern_set.index(pattern[i])]:
            return False
    return True


def main():
    print(wordPattern("aabb", ["elice", "elice", "alice", "alice"]))  # should return True
    print(wordPattern("abab", ["elice", "elice", "alice", "alice"]))  # should return False


if __name__ == "__main__":
    main()
