# time complexity: O(n^2) - the outer loop runs n times and the inner loop runs n - sorted_item_count - 1 times
# space complexity: O(1) - in-place sorting
def bubble_sort(arr):
    n = len(arr)
    for sorted_item_count in range(n):
        for i in range(0, n - sorted_item_count - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]