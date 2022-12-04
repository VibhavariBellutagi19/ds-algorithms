# Introduction: Insertion sort, sorts the array from the left side
# tricks: 
# Output: 
# Input:
# Time complexity: O(N^2)
# Why insertion sort? -> adaptive in nature, steps gets reduced if the array is sorted ( j breaks if j > j-1)
#                        it is stable algorithm
#                        used of smaller values of N, works well when array partially sorted

def insertion_sort(arr):

    for i in range(len(arr) - 1):
        j = i + 1
        while(j > 0):
            if(arr[j] < arr[j-1]):
                swap(arr, j, j-1)
                j -= 1
            else:
                break
def swap(arr, firstElement, secondElement):
    arr[firstElement], arr[secondElement] =  arr[secondElement], arr[firstElement]
    return arr

def main():
    arr = [4,3,5,1,2]

    print("Array before sorting: {}".format(arr))

    insertion_sort(arr)

    print("Array after sorting: {}".format(arr))



if __name__ == "__main__":
        main()