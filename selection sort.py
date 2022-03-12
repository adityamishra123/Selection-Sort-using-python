def selection_sort(arr):
    for i in range(len(arr)):
        min=i
    for j in range(i+1 ,len(arr)):
        if arr[j]<arr[min]:
          min=j
    arr[min],arr[i]=arr[i],arr[min]
    return arr
num_arr=[11,1,77,84,9]
print("array before sorting:")
print(num_arr)

selection_sort(num_arr)

print("\narray after sorting:")
print(num_arr)