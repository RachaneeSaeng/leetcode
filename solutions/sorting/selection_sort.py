# time complexity: O(n^2) - the outer loop runs n times and the inner loop runs n - i times
# space complexity: O(1) - in-place sorting
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]