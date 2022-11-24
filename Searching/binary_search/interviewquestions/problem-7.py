# Introduction: Search in Rotated Sorted Array (https://leetcode.com/problems/search-in-rotated-sorted-array/)
# tricks: Binary search is applied to sorted array in 90% of time. if it is sorted array, try binary search first. but no target
# Output: 4
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Time complexity: 

def get_pivot(arr, start, end):

    while(start <= end):
        mid = start + (end-start)//2

        # case 1: if arr[mid] > arr[mid+1]
        if (mid < end and arr[mid] > arr[mid+1]):
            return mid
        
        # case 2: if arr[mid] < arr[mid - 1]
        if (mid > start and arr[mid] < arr[mid - 1]):
            return mid - 1
        
        # case 3: if arr[mid] <= arr[start]
        if arr[mid] <= arr[start]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def binary_search(arr,start,end,target):

    while(start <= end):
        mid = start + (end-start)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def search_element(arr, target):
    start = 0
    end = len(arr) - 1

    if(len(arr) == 1 and arr[0] != target):
        return -1

    # find pivot
    pivot = get_pivot(arr,start,end)
    if pivot == -1:
        print("Pivot not found")
    else:
        print("Pivot found at position: {}".format(pivot))

    if(pivot == -1):
         element = binary_search(arr, start, end, target)
         return element
    if(arr[pivot] == target):
         return pivot
    if(target >= arr[start]):
         return binary_search(arr,0,pivot - 1, target)
    else:
        return binary_search(arr, pivot + 1, end, target)


def main():
    arr = [4,5,6,7,0,1,2]
    target = 2

    res = search_element(arr, target)
    if res == -1:
        print("Element not found")
        print(res)
    else:
        print("Element found at position: {}".format(res))
    

if __name__ == "__main__":
        main()