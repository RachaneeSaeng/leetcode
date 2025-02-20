# time complexity: O(n^2) - the outer loop runs n times and the inner loop runs i times
# space complexity: O(1) - in-place sorting
def insertion_sort(arr):
    for target_index in range(1, len(arr)):
        target_value = arr[target_index]
        checking_idx = target_index - 1
        while checking_idx >= 0 and arr[checking_idx] > target_value:
            arr[checking_idx + 1] = arr[checking_idx]
            checking_idx -= 1
        arr[checking_idx + 1] = target_value