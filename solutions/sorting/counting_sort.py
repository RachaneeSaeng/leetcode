# time complexity: O(k + n) - counting the occurrences of each element in the input array takes O(k) time and building the output array takes O(n) time
# space complexity: O(k + n) - the count_arr and output_arr both have a length of n
def counting_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    # count the occurrences of each element in the input array
    # first index of count_arr corresponds to the min_val
    for num in arr:
        idx_of_num = num - min_val
        count_arr[idx_of_num] += 1

    # accumulate the count of elements in the count_arr
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # build the output array by placing number in the correct position based on the accumulated count
    for num in arr:
        acc_idx_of_num = num - min_val
        sorted_idx_of_num = count_arr[acc_idx_of_num] - 1
        output_arr[sorted_idx_of_num] = num
        
        count_arr[acc_idx_of_num] -= 1

    return output_arr