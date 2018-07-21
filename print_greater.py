# print_greater
def main():
    pass
    a,b = input().split(' ')
    if len(a)>len(b):
        print(a)
    elif(len(a)<len(b)):
        print(b)
    else:
        print(a or b)

if __name__ == '__main__':
    main()
