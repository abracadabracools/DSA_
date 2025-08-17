arr = [3, 5, 2, 9, 4]
maximum = max(arr)
print("The maximum value is:", maximum)

# This code finds the maximum value in an array and prints it.
# The maximum value is: 9
# This code snippet finds the maximum value in an array and prints it.  

def find_maximum(arr):
    """Function to find the maximum value in an array."""
    if not arr:
        return None
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum

# Example usage 
if __name__ == "__main__":
    example_array = [3, 5, 2, 9, 4]
    print("The maximum value is:", find_maximum(example_array))
    # Output: The maximum value is: 9