def swap_case(s):
    case_c=''
    for i in s:
        if i.isupper():
            case_c += i.lower()
        elif i.islower():
            case_c += i.upper()
        else:
            case_c += i
    return case_c

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)