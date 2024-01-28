def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def find_sorted_position(arr, k):
    n = len(arr)
    quicksort(arr, 0, n - 1)
    return sorted(range(n), key=lambda x: arr[x])[k] + 1

# Input
# T = int(input())
# for _ in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
arr=[2,-2,8,9]  
K=2 
result = find_sorted_position(arr, K)
print(result)
