def selection_sort(arr):
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker, len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
        spot_marker += 1
        print(arr)
l = [2, 9, 5, 10, 10, 1, 8, 4, 3, 6, 7]
selection_sort(l)

# start iteration 0:    2, 9, 5, 10, 10, 1, 8, 4, 3, 6, 7

#   [1, 9, 5, 10, 10, 2, 8, 4, 3, 6, 7]
#   [1, 2, 9, 10, 10, 5, 8, 4, 3, 6, 7]
#   [1, 2, 3, 10, 10, 9, 8, 5, 4, 6, 7]
#   [1, 2, 3, 4, 10, 10, 9, 8, 5, 6, 7]
#   [1, 2, 3, 4, 5, 10, 10, 9, 8, 6, 7]
#   [1, 2, 3, 4, 5, 6, 10, 10, 9, 8, 7]
#   [1, 2, 3, 4, 5, 6, 7, 10, 10, 9, 8]
#   [1, 2, 3, 4, 5, 6, 7, 8, 10, 10, 9]
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]