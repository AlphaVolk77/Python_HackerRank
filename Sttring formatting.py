def print_formatted(number):
    l1=len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(l1,' '),end=" ")
        print(oct(i).replace("0o","").rjust(l1,' '),end=" ")
        print(hex(i).replace("0x","").upper().rjust(l1,' '),end=" ")
        print(bin(i).replace("0b","").rjust(l1,' '),end=" ")
        print("")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)