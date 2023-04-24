# def findSmallest(arr):
#     smallest = 0
#     smallest_value = arr[0]

#     for i in range(1, len(arr)):
#         if arr[i] < smallest_value:
#             smallest = i
#             smallest_value = arr[i]

#     return smallest


# def selection_sort(arr):
#     new_arr = []

#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         new_arr.append(arr.pop(smallest))

#     return new_arr


# my_list = [345, 23, 1235, 5667, 6, 83, 664]

# print(selection_sort(my_list))


def smallest(arr):
    smallest_index = 0
    smallest_value = arr[smallest_index]

    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_index = i
            smallest_value = arr[i]

    return smallest_index


def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        new_arr.append(arr.pop(smallest(arr)))

    return new_arr


newer_list = [4, 1, 66, 4, 2, 50, 717, 34, 18, 91]

print(selection_sort(newer_list))
