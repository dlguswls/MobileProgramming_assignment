from random import randrange

class FunnyDice :
    def __init__(self, n = 6):
        self.n = int(n)
        self.numbers = list(range(1,n+1))
        self.index = randrange(0,self.n)
        self.val = self.numbers[self.index]
    def throw(self):
        self.index = randrange(0,self.n)
        self.val = self.numbers[self.index]
    def getval(self):
        return self.val
    def setval(self):
        if val <= self.n :
            slef.val = val
        else :
            msg = "주사위에 없는 숫자입니다. 주사위는 1 ~ {0}까지 있습니다.".format(self.n)
            raise ValueError(msg)

def get_inputs() :
    n = int(input('주사위 면의 개수를 입력하세요: '))
    return n

def main() :
    n = get_inputs()
    mydice = FunnyDice(n)
    mydice.throw()
    print("행운의 숫자는? {}".format(mydice.getval()))

if __name__ == '__main__' :
    main()
    
    
