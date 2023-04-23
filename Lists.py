if __name__ == '__main__':
    N = int(input())
    l = list()
    for i in range(N):
        cmd,*num = input().split()
        num=list(map(int,num))
        if(cmd == 'insert'):
            l.insert(num[0],num[1])
        elif(cmd == 'print'):
            print(l)
        elif(cmd == 'remove'):
            l.remove(num[0])
        elif(cmd == 'append'):
            l.append(num[0])
        elif(cmd == 'sort'):
            l.sort()
        elif(cmd == 'pop'):
            l.pop()
        elif(cmd == 'reverse'):
            l.reverse()