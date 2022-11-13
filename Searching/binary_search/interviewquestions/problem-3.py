# Introduction: https://leetcode.com/problems/find-smallest-letter-greater-than-target/ with letter wrapping around
# tricks: Binary search is applied to sorted array in 90% of time. if it is sorted array, try binary search first.
# 1. Ceiling of a number
# 2. Ignore the target = what we are looking for
# 3. ["c","f","j"], target = "j" -> there's no character large than target element.
# 4. start will be length of the index. start % len(array) => will be always 0
# Output: 
# Input: ["c","f","j"], target = "a"
# Time complexity:


def nextGreatestLetter(arr,target,start,end):
    
    while(start <= end):
        mid = start + (end-start)//2
        if target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    return arr[start % len(arr)]

def main():
    arr = ["c","f","j"]
    target = "a"
    start = 0
    end = len(arr) - 1
    res = nextGreatestLetter(arr,target,start,end)
    print(res)

if __name__ == "__main__":
    main()