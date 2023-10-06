def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Flag to optimize the algorithm by breaking if no swaps are made
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap arr[j] and arr[j+1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps are made in a pass, the list is already sorted
        if not swapped:
            break
    return arr
