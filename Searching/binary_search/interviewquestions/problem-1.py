# Introduction: Ceiling of a given number. smllest element in array which is >= target
# tricks: Binary search is applied to sorted array in 90% of time. if it is sorted array, try binary search first.
# 1. find target
# 2. find all numbers >= target
# 3. find the smallest among numbers >= target
# Output: 
# Input: [2,3,5,9,14,16,18]
# Time complexity: 

def ceil_number(arr,target,start,end):
    
    while(start <= end):
        mid = start + (end-start)//2
        if target >= arr[mid]:
            start = mid + 1
            ans = start # start and end pointers are two pointers, where ans will be lying between s and e.
            #when while condition is voilated, the target would between end and start. so start is the answer.
            # usually -> s.   ans.   end
            # here -> end.   ans.   s ( next big number when no answer found is start )
        elif target < arr[mid]:
            end = mid - 1
    return ans

def main():
    arr = [0,2,3,5,9,14,16,18]
    target = 1
    start = 0
    end = len(arr) - 1
    res = ceil_number(arr,target,start,end)
    print(res)

if __name__ == "__main__":
        main()