# Python3 program to sort an array
# using hash function
def sortUsingHash(a, n):
    # find the maximum element
    Max = max(a)

    # create a hash function upto
    # the max size with every element equals to 0
    Hash = [0] * (Max + 1)
    # traverse through all the elements
    # and keep a count
    for i in range(0, n):
        Hash[a[i]] += 1

    # Traverse upto all elements and check
    # if it is present or not. If it is
    # present, then print the element the
    # number of times it's present. Once we
    # have printed n times, that means we
    # have printed n elements so break out
    # of the loop
    # for i in range(0, Max + 1):
    #
    #     # if present
    #     if Hash[i] != 0:
    #
    #         # print the element that number
    #         # of times it's present
    #         for j in range(0, Hash[i]):
    #             print(i, end=" ")
    return Hash







                # Driver Code
if __name__ == "__main__":

    a = [6, 7, 8, 9, 11, 6, 8, 14, 16, 17]
    n = len(a)

    print(sortUsingHash(a, n))
