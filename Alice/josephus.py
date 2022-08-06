import queue

def josephus(num, target):
    q = queue.Queue()
    for i in range(1, num+1):
        q.put(i)
    result = []
    while q.qsize() > 0 :
        for i in range(target-1) :
            a = q.get()
            q.put(a)
        result.append(q.get())
    return result

def main():
    print(josephus(7, 3)) #[3, 6, 2, 7, 5, 1, 4]이 반환되어야 합니다

if __name__ == "__main__":
    main()