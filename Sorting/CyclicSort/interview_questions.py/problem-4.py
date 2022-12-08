# Introduction: https://leetcode.com/problems/set-mismatch/
# tricks:
# Output: 
# Input:
# Time complexity:

def cyclic_sort(arr):
    n = len(arr)
    i = 0

    while(i < n):
        correct = arr[i] - 1
        if(arr[i] != arr[correct]):
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    return arr

def findErrorNums(arr):
    missing_numbers = []
    for i in range(len(arr)):
        if i != arr[i] - 1:
            missing_numbers = [i+1, arr[i]]
        else:
            i += 1
    return missing_numbers

def main():
    arr = [3,2,2]
    cyclic_sort(arr)
    errorNum = findErrorNums(arr)
    print("errorNum: {}".format(errorNum))

if __name__ == "__main__":
    main()