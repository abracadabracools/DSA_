def delete_duplicates(nums):
    """
    Removes duplicates from a sorted array in-place.
    Returns the length of the array after duplicates have been removed.
    """
    if not nums:
        return 0

    write_index = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index

# Example usage:
arr = [1, 1, 2, 2, 3, 4, 4, 5]
length = delete_duplicates(arr)
print(arr[:length])  # Output: [1, 2, 3, 4, 5]