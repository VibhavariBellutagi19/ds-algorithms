# Introduction: Binary search is used for sorted array
# tricks: find the middle element
#         target > mid => right else left
#          middle == target => element found
# Input: 2,4,6,10,18,19,20,45,56,67,78,89
# Output: 
# Time complexity: 

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


def main():
    arr = [2,4,6,10,18,19,20,45,56,67,78,89]
    start = 0
    end = len(arr) - 1
    target = 99

    result = binary_search(arr, start, end, target)
    if result == -1:
        print(" Element not found")
    else:
        print(" Element found at position: {}".format(result))



if __name__ == "__main__":
        main()