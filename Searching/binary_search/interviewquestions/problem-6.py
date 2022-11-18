# Introduction: Moutain array (https://leetcode.com/problems/peak-index-in-a-mountain-array/)
# tricks: Binary search is applied to sorted array in 90% of time. if it is sorted array, try binary search first. but no target
# 1) if the e[mid] > e[mid+1] -> decreasing part of array
# 2) if the e[mid] < e[mid+1] -> ascending part of array
# Output: 1, 2
# Input: [0,1,0] , [0,2,1,0]
# Time complexity: O(logn)

def find_moutain(arr):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = start + (end-start)//2
        if arr[mid] > arr[mid + 1]:
            end = mid
        elif arr[mid] < arr[mid + 1]:
            start = mid
            ans = start
    return mid
        

def main():
    arr = [0,2,1,0]

    res = find_moutain(arr)
    print(res)
    

if __name__ == "__main__":
        main()