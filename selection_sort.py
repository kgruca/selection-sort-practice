def findSmallest(arr):
    smallest = 0
    smallest_value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest = i
            smallest_value = arr[i]

    return smallest


def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallest = findSmallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr


my_list = [345, 23, 1235, 5667, 6, 83, 664]

print(selection_sort(my_list))
