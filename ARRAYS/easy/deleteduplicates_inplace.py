

def main(arr):
    s=1
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            arr[s] = arr[i]
            s+=1
    return s


if __name__ == "__main__":
    arr = [1,1,1,2,2,2,3,4,5,5,6]
    s = main(arr)

    print(f'the non repeated array is {arr[:s]} ')