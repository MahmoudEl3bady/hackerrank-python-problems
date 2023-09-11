def swap_case(s):
    lst=[]
    for i in s :
        if i.isupper():
            lst+=i.lower()
        else:
            lst+=i.upper()

             
    return ''.join(lst)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)