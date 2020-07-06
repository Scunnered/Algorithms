def merge_sorted(arr1,arr2):
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2)
        if arr[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        print(sorted_arr)
    return sorted_arr

# Program execution
l1 = [2,4,6,8]
l2 = [1,3,5,7,8,9,10]
print(f"Merged list: {merge_sorted (l1,l2)}")