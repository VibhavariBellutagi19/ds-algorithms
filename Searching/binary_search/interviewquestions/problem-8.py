# Introduction: Search in Rotated Sorted Array with duplicates (https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
# tricks: Binary search is applied to sorted array in 90% of time. if it is sorted array, try binary search first. but no target
# Output: true
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Time complexity: 

def get_pivot_with_duplicates(arr, start, end):

    while(start <= end):
        mid = start + (end-start)//2

        # case 1: if arr[mid] > arr[mid+1]
        if (mid < end and arr[mid] > arr[mid+1]):
            return mid
        
        # case 2: if arr[mid] < arr[mid - 1]
        if (mid > start and arr[mid] < arr[mid - 1]):
            return mid - 1
        
        # case 3: if start == end == mid, we can skip
        if(arr[mid] == arr[start] and arr[mid] == arr[end]):
            if(start < end and arr[start] > arr[start + 1]):
                return start
            start += 1
            if(end > start and arr[end] < arr[end - 1]):
                return end
            end -= 1
        if(arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] < arr[end])):
            start = mid + 1
        else:
            end = mid - 1

        
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
    pivot = get_pivot_with_duplicates(arr,start,end)
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
    arr = [2,5,6,0,0,1,2]
    target = 0

    res = search_element(arr, target)
    if res == -1:
        print("False")
    else:
        print("True")
    

if __name__ == "__main__":
        main()