# Introduction: floor of a given number. biggest element in array which is <= target
# tricks: Binary search is applied to sorted array in 90% of time. if it is sorted array, try binary search first.
# 1. find target
# 2. find all numbers <= target
# 3. find the greatest among numbers <= target
# Output: 
# Input: [2,3,5,9,14,16,18]
# Time complexity: 

def ceil_number(arr,target,start,end):
    
    while(start <= end):
        mid = start + (end-start)//2
        if target > arr[mid]:
            start = mid + 1
        elif target <= arr[mid]:
            end = mid - 1
            ans = end
    return ans

def main():
    arr = [0,2,3,5,9,14,16,18]
    target = 17
    start = 0
    end = len(arr) - 1
    res = ceil_number(arr,target,start,end)
    print(res)



if __name__ == "__main__":
        main()