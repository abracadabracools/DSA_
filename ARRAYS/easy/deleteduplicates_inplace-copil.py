
arr = [1,1,1,2,2,2,3,4,5,5,6]
i = 1
while i < len(arr):
    if arr[i] == arr[i-1]:
        del arr[i]
    else:
        i += 1
print(arr)