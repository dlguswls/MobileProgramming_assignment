def isParenthesisValid(st):
    stack = []
    pDict = {'}':'{', ')':'(', '>':'<', ']':'['}
    pOpens = ('(','[','{','<')
    for ch in st :
        if ch in pOpens :  # ch가 열린 괄호
            stack.append(ch)
        else : # ch가 닫힌 괄호호
            if len(stack) !=0 and stack[-1] == pDict[ch] :
                stack.pop()
            else :
                return False
    if len(stack) != 0 :
        return False
    return True


def main():
    examples = ["({()})", "[]<>{}", ")(" "<]", "<(>)"]
    for example in examples:
        print(example, isParenthesisValid(example))


if __name__ == "__main__":
    main()