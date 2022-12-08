# Pattern-5
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

def print_pattern(n):

    for row in range(1, 2 * n):
        if row > n:
            no_of_col_in_row = (2 * n) - row
        else:
            no_of_col_in_row = row
        for col in range(1, no_of_col_in_row + 1):
            print("*", end=" ")
        print()
        
def main():
    n = 5
    print_pattern(n)


if __name__ == "__main__":
        main()