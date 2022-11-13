# Introduction: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# tricks: Binary search is applied to sorted array in 90% of time. if it is sorted array, try binary search first.
# 1. find the firt occurence of given target
# 2. 
# Output: [3,4]
# Input: [5,7,7,8,8,10]  target = 8
# Time complexity:

def searchRange(arr,target):
    result = [-1,-1]
    
    result[0] = search(arr, target, True)
    result[1] = search(arr, target, False)

    return result

def search(arr, target, findstart):

    ans = -1
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = start + (end-start)//2
        if target == arr[mid]:
            ans = mid
            if(findstart):
                end = mid - 1
            else:
                start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return ans

def main():
    arr = [5,7,7,8,8,8,8,10]
    target = 8
    res = searchRange(arr,target)
    print(res)

if __name__ == "__main__":
    main()