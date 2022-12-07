# Introduction: Cyclic sort when given array has integers 1 to N
# tricks: Check if the number is at correct index, if yes move i pointer else swap it with correct index
#         To find the correct index, index = value - 1
# Output:
# Input:
# Time complexity: O(N)

def cyclic_sort(arr):
    # loop through N - 1 lenght of array
    index = 0
    while (index < len(arr)):
        # correct index that number ( arr[i] ) should be present
        correct = arr[index]-1
        # if current element ( arr[index] ) is not present in its correct index - arr[correct], then swap
        if(arr[index] != arr[correct]):
            # swapping the index
            swap(arr, index, correct)
        else:
            index += 1

    return arr


def swap(arr, firstElement, secondElement):
    temp = arr[firstElement]
    arr[firstElement] = arr[secondElement]
    arr[secondElement] = temp


def main():
    arr = [3, 5, 3, 1, 4]

    print("Array before sorting: {}".format(arr))

    cyclic_sort(arr)

    print("Array after sorting: {}".format(arr))


if __name__ == "__main__":
    main()
