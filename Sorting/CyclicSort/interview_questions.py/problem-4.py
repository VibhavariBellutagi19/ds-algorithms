# Introduction: https://leetcode.com/problems/set-mismatch/
# tricks:
# Output: 
# Input:
# Time complexity:

def findErrorNums(arr):
    missing_numbers = []
    for i in range(len(arr)):
        if i != arr[i] - 1:
            missing_numbers = [i, i+1]
        else:
            i += 1
    return missing_numbers

def main():
    arr = [1,2,3,3,5]

    errorNum = findErrorNums(arr)
    print("errorNum: {}".format(errorNum))

if __name__ == "__main__":
    main()