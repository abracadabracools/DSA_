def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# Example usage:
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))  # Output: True

arr2 = [5, 3, 2, 1]
print(is_sorted(arr2))  # Output: False