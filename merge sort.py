def merge_sorted(arr1,arr2):
    print("Merge function called with the lists below")
    print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        print(sorted_arr)
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

# Program execution
l1 = [1,3,5,7,8,9,10]
l2 = []
print(f"Merged list: {merge_sorted(l1,l2)}")