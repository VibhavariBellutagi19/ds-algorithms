# Introduction: Searching in sorted matrix using binary search
# tricks: 
    # 1. Linear search
    # 2. Convert it into 1D array and apply binary search
    # 3. Apply BS
        # 1.Take middle column and perform BS on it ( trying to resuce the rows)
        # 2. If element == target: return ans
        # 3. If element > target: ignore below rows
        # 4. If element < target: ignore above rows
        # 5. lower bound = first row and upper bound = last row
# Output: 
# Input: [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# Time complexity: 


def binary_search(arr,row,c_start,c_end,target):
    '''
    Search in the row provided in the column provided
    c_start = column start
    c_end = column end
    which row
    '''

    while(c_start <= c_end):
        mid = c_start + (c_end - c_start)//2
        if arr[row][mid] == target:
            return [row, mid]
        elif target < arr[mid]:
            c_end = mid - 1
        else:
            c_start = mid + 1
    return [-1, -1]

def search(arr, target):
    pass


def main():
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    


if __name__ == "__main__":
        main()