import time
import random

def bubble_sort(arr):
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    # Generate a list of 100 random numeric values
    random_list = [random.randint(1, 1000) for _ in range(100)]

    # Bubble sort
    start = time.perf_counter()
    bubble_sort(random_list.copy())
    print("Bubble Sort: %.6f milliseconds" % ((time.perf_counter() - start) * 1000))

    # Selection sort
    start = time.perf_counter()
    selection_sort(random_list.copy())
    print("Selection Sort: %.6f milliseconds" % ((time.perf_counter() - start) * 1000))

    # Insertion sort
    start = time.perf_counter()
    insertion_sort(random_list.copy())
    print("Insertion Sort: %.6f milliseconds" % ((time.perf_counter() - start) * 1000))

if __name__ == "__main__":
    main()