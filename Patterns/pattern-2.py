# Pattern-2
# *
# * *
# * * *
# * * * *


def print_pattern(n):
    # outer for loop to print the numbers of rows
    for row in range(1, n+1):
        # inner loop for number of columns for every row
        for col in range(1, row + 1):
            # what to print
            print("*", end=' ')
        print()

def main():
    n = 5
    print_pattern(n)


if __name__ == "__main__":
        main()