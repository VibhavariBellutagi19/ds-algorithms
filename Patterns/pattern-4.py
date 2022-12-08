# Pattern-2
# 1
# 1 2
# 1 2 3
# 1 2 3 4


def print_pattern(n):
    counter = 0
    # outer for loop
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            counter += 1
            print(counter, end=" ")
        counter = 0
        print()

def main():
    n = 5
    print_pattern(n)


if __name__ == "__main__":
        main()