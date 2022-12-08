# Pattern-2
# * * * *
# * * * *
# * * * *
# * * * *

def print_pattern(n):

    for row in range(1, n + 1):
        for col in range(1, n + 1):
            print("*", end=" ")
        print()
        
def main():
    n = 5
    print_pattern(n)


if __name__ == "__main__":
        main()