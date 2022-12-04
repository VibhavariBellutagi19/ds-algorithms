# Introduction: 
# tricks: j runs from lenght(arr) - i - 1
# Output: 
# Input:
# Time complexity: 


def bubble_sort(arr):
    n = len(arr)
    # we know that if the array is sorted, there wont be any swaps required
    swapped = False
    # outer loop runs from 0 to n-1, because last pass would be sorted
    for i in range(0, n):
        # inner loop runs from 1 to n-i-1, because for every run, the largestest number would be sorted at end
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
        if(not swapped): break
    return arr


def main():
    arr = [1,2,3,4,5]

    print("Array before sorting: {}".format(arr))

    bubble_sort(arr)

    print("Array after sorting: {}".format(arr))



if __name__ == "__main__":
        main()