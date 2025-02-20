def quick_sort(array, low, high):
    if low < high:
        # pi is partitioning index
        pi = partition(array, low, high)
        
        # Separately sort elements before and after partition
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

def partition(array, low, high):
    pivot = array[high]    # Choose rightmost element as pivot
    i = low - 1            # Index of smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if array[j] <= pivot:
            i += 1      # Increment index of smaller element
            array[i], array[j] = array[j], array[i]  # Swap
    
    array[i + 1], array[high] = array[high], array[i + 1]  # Place pivot in correct position
    return i + 1           # Return pivot's final position

# Example usage
if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    n = len(array)
    quick_sort(array, 0, n - 1)
    print("Sorted array is:", array)