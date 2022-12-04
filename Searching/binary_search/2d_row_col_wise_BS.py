# Introduction: Binary search is used for sorted array. the matix is sorted row wise and col wise
# Search something try to see how you can reduce the search space
# tricks: eleminate rows and columns
# start searching from frist row and last column ( lower bound = row 0 and upper bound = last col)
# Input: 
# Output: 
# Time complexity: N rows + N cols = O(2N) = O(N)

def row_col_binary_search(arr,target):
    row = 0
    col = len(arr) - 1

    while(row < len(arr) and col >= 0):
        if arr[row][col] == target:
            return [row, col]
        elif arr[row][col] > target:
            col -=1
        else:
            row +=1
    return [-1, -1]


def main():
    arr = [[10,20,30,40],[15,25,35,45],[28,29,37,49],[33,34,38,50]]
    target = 30

    result = row_col_binary_search(arr,target)
    if result == -1:
        print(" Element not found")
    else:
        print(" Element found at position: {}".format(result))



if __name__ == "__main__":
        main()