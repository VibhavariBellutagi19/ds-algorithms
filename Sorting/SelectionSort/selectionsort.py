# Introduction: 
# tricks: 
    # find the max element in the array, swap it with the correct index
# Output: 
# Input:
# Time complexity: O(N^2)
# Only works fine when we have small list


def selection_sort(arr):
   
   for i in range(len(arr)):
        lastIndex = len(arr) - i - 1
        maxIndex = getMaxIndex(arr, 0, lastIndex)
        swap(arr, maxIndex, lastIndex)

def getMaxIndex(arr, start, end):
    maxIndex = start

    for i in range(start, end+1):
        if arr[i] > arr[maxIndex]:
            maxIndex = i
    return maxIndex

def swap(arr, firstElement, secondElement):
    arr[firstElement], arr[secondElement] =  arr[secondElement], arr[firstElement]
    return arr

def main():
    arr = [5,4,3,2,1]

    print("Array before sorting: {}".format(arr))

    selection_sort(arr)

    print("Array after sorting: {}".format(arr))



if __name__ == "__main__":
        main()