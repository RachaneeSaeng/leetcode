# make the sub array to be a max heap and ensuring the element at the i index is the largest element in the array
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1 #left child
    right = 2 * i + 2 #right child

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
# time complexity: O(nlogn) - building the heap takes O(n) time and heapify takes O(logn) time
# space complexity: O(1) - in-place sorting
def heap_sort(arr):
    n = len(arr)

    # building a max-heap from the input array by calling heapify on each non-leaf node, 
    # starting from the last non-leaf node (n // 2 - 1) and moving up to the root (0)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # repeatedly extracts the maximum element (the root of the heap) and places it at the end of the reduced array
    # then calls heapify on the reduced heap to restore the heap property
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)