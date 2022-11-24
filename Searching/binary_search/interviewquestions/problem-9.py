# Introduction: Given an array arr[] of size N having distinct numbers sorted in increasing order and the array has been right rotated (i.e, the last element will be cyclically shifted to the starting position of the array) k number of times, the task is to find the value of k.
# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
# tricks: Binary search is applied to sorted array in 90% of time. if it is sorted array, try binary search first. but no target
# Output: 4
# Input: nums = {7, 9, 11, 12, 5}
# Time complexity: 

def count_elements(arr):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = start + (end - start)//2
        if(mid < end and arr[mid] > arr[mid+1]):
            return mid
        if(mid > start and arr[mid] < arr[mid-1]):
            return mid - 1
        
        if(arr[mid] <= arr[start]):
            end = mid - 1
        else:
            start = mid + 1
    return -1

def main():
    arr = [5, 7, 9, 11, 12]

    count = count_elements(arr)
    if count == -1:
        print("Rotation count - 0")
    else:
        print("Rotation count - {}".format(count+1))
    

if __name__ == "__main__":
        main()