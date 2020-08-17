import math

arr = [4, 8, 10, 15, 18, 21, 24, 27, 29, 33, 34, 37, 39, 41, 43]


def binary_search(arr, l, h, key):
    arr.sort()
    if l <= h:
        mid = math.floor((l + h) / 2)
         
        if key == arr[mid]:
            print('found at\n')
            print(mid)
        elif key < arr[mid]:
            binary_search(arr, l, mid-1, key)
        else:
            binary_search(arr, mid+1, h, key)
    else:
        print('not found')

binary_search(arr, 0, len(arr)-1, 8)
# non recursively
# def binary_search(arr, key):
#     l = 0
#     h = len(arr) - 1
#     while l <= h:
#         mid = math.floor((l + h) / 2)
#         key = 18
#         if key == arr[mid]:
#             print('found at\n')
#             print(mid)
#             break
#         elif key < arr[mid]:
#             h = mid - 1
#         else:
#             l = mid + 1
#
#
#     return -1
#
# binary_search(arr, 18)