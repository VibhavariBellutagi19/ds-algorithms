def arrangeCoins(n: int):
        # Binary Search with Gauss Formula
        # to find the number of coins needed in each rows of n use formula
        # n // 2 (n + 1)

        # We know the min coin/row would be n > 0 always
        start = 1

        # Also we know that the max rows can be = n
        end = n

        # to find the number of coins
        res = 0

        while(start <= end):
            # find mid, this says how many rows can be formed
            mid = start + (end - start)//2

            # find the number of coins with mid rows
            coins = (mid / 2 ) * (mid + 1)

            if coins > n:
                end = mid - 1
            else:
                start = mid + 1
                res = mid
        return res

print(arrangeCoins(5))
