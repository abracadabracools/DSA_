
def find_if_sorted(arr):
    prev= arr[0]
    for curr in arr:
        if curr<prev:
            print('Not sorted')
            return
        prev = curr
    print('sorted')

if __name__== '__main__':
    arr = [-6,-5]
    find_if_sorted(arr)

