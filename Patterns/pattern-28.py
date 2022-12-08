# Pattern-28 - diamond - https://github.com/kunal-kushwaha/DSA-Bootcamp-Java/blob/main/assignments/09-patterns.md
def print_pattern(n):

    for row in range(1, 2 * n):
        if row > n:
            no_of_col_in_row = (2 * n) - row
        else:
            no_of_col_in_row = row
        
        spaces = n - no_of_col_in_row
        for i in range(1, spaces + 1):
            print(end=" ")

        for col in range(1, no_of_col_in_row + 1):
            print("*", end=" ")
        print()
        
def main():
    n = 5
    print_pattern(n)


if __name__ == "__main__":
        main()