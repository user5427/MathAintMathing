def find(array: list[int], target: int) -> int:
    left = 0
    right = len(array) - 1 # 4

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid - 1
        else:
            right = mid + 1

    return -1

test = find([1,3,4,5,7], 5)
print(test)  