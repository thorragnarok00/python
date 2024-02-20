import time
import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

def main():
    # Generate a list of 100 random numeric values
    random_list = [random.randint(1, 1000) for _ in range(100)]

    # Quick sort
    start = time.perf_counter()
    quick_sort(random_list.copy(), 0, len(random_list) - 1)
    print("Quick Sort: %.6f milliseconds" % ((time.perf_counter() - start) * 1000))

    # Merge sort
    start = time.perf_counter()
    merge_sort(random_list.copy(), 0, len(random_list) - 1)
    print("Merge Sort: %.6f milliseconds" % ((time.perf_counter() - start) * 1000))

if __name__ == "__main__":
    main()