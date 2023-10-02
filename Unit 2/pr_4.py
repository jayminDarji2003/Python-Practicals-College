# Write a program to sort an array using bubble sort.

def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]

arr = [1,17,7,4,3,10,44,89]
bubble_sort(arr)
print("sorted array : ", arr)
