# Introduction: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# tricks: Binary search is applied to sorted array in 90% of time. if it is sorted array, try binary search first. but no target
# Output: 1
# Input: nums = [3,4,5,1,2]
# Time complexity: 

def pivot_element(arr):
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
    arr = [4,5,6,7,0,1,2]

    pivot = pivot_element(arr)
    if pivot == -1:
        print(arr[0])
    else:
        print(arr[pivot + 1])
    

if __name__ == "__main__":
        main()