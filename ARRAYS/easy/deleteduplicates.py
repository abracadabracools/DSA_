
def delete_duplicates(arr):
    new_arr = []
    prev = arr[0]
    new_arr.append(prev)
    for curr in arr:
        if curr==prev:
            pass
        else:
            new_arr.append(curr)
            prev=curr
    print(f' New Array  = {new_arr}')

if __name__=="__main__":
    arr = [1, 1, 2,2, 3, 4, 5, 6, 6, 6]
    print(f' OLD Array  = {arr}')
    delete_duplicates(arr)

