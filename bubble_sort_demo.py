def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        print('Bubble sort result ' +str(arr))
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)

# Start Iteration 0:    6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5
# After Iteration 1:    6, 1, 4, 8, 7, 8, 9, 3, 2, 5, 10
# After Iteration 2:    1, 4, 6, 7, 8, 8, 3, 2, 5, 9, 10
# Sorted list:          1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10