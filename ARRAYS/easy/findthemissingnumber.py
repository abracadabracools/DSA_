
def main(arr):
    # print(1 ^ 2 ^ 3 ^ 4 ^ 5)
    # print(1 ^ 2 ^ 4 ^ 5)
    # print((1 ^ 2 ^ 3 ^ 4 ^ 5)^(1 ^ 2 ^ 4 ^ 5))
    max_= max(arr)
    xor=0
    xor_=0
    for i  in range(1,max_+1):
            xor ^=i
    for i in arr:
            xor_^=i

    missing_numb = xor_ ^ xor

    print(f'missing_numb - {missing_numb}')



if __name__=='__main__':
    arr = [1,3,4,5,6]
    main(arr)