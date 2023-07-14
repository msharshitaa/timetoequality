def calculate_time_to_equality(arr):
    arr.sort()
    end = arr[-1]
    time = 0
    for i in range(len(arr)-1):
        time += end - arr[i]
    return time
arr = list(map(int, input().strip().split()))
print(calculate_time_to_equality(arr))
