# Introduction: Find position of an element in a sorted array of infinite numbers
# tricks: Binary search is applied to sorted array in 90% of time. if it is sorted array, try binary search first.
# 1. Infinite array - no start and end
# 2. find the start and end where the index lies. keep finding the ranging ( start and end chunk )
# 3. multiple exponentially
# Output: 
# Input:
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

def get_ans(arr, target):
    pass

    
def main():
    arr = [2,4,6,10,18,19,20,45,56,67,78,89]
    



if __name__ == "__main__":
        main()