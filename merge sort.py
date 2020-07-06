def merge_sorted(arr1,arr2):
    print("Merge function called with lists below:")
    print(f"left: {arr1} and right: {arr2}")
    sorted_arr = []
    i, j = 0, 0
    if arr[i] < arr2[j]:
        sorted_arr.append(arr1[i])
        i += 1
    else:
        sorted_arr.append(arr2[j])
        j += 1
    print(f"Left list index i is {i} and has value: {arr1[i]}")
    print(f"Right list index j is {j} and has value: {arr2[j]}")
    return sorted_arr

# Program execution
l1 = [2,4,6,8,10]
l2 = [1,3,5,7,8,9]
print(f"Un-merged list: {merge_sorted (l1,l2)}")