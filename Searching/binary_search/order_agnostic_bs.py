# Introduction: Binary search is used for sorted array
# tricks: to find if the array is sorted or not in ascending order.
# Output: 
# Input: 2,4,6,10,18,19,20,45,56,67,78,89
# Time complexity: 

def binary_search_desc(arr, start, end, target):
    while(start <= end):
        mid = start + (end-start)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def binary_search_ascending(arr, start, end, target):
    while(start <= end):
        mid = start + (end-start)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def main():
    arr = [90,89,79,67,45,34,23,12,11,1]
    start = 0
    end = len(arr) - 1
    target = 67

    # sorted in ascending or descending order
    if arr[start] < arr[end]:
        print("Array is sorted in Ascending order")
        result = binary_search_ascending(arr, start, end, target)
    else:
        print("Array is sorted in Descending order")
        result = binary_search_desc(arr, start, end, target)
    
    if result == -1:
        print("Element not found")
    else:
        print("Element found at position: {}".format(result))



if __name__ == "__main__":
        main()