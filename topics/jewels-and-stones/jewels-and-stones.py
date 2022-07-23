# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    """
    - can stones be empty?
    - can jewels be repeated?
    """

    # sets
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        if not stones:
            return 0

        jewels = set(jewels)

        return sum(s in jewels for s in stones)

        # straightforward

    def numJewelsInStones3(self, jewels: str, stones: str) -> int:
        if not stones:
            return 0

        count = 0

        for jewel in jewels:
            count += stones.count(jewel)

        return count

    # straitforward
    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        if not stones:
            return 0

        count = 0

        for stone in stones:
            if stone in jewels:
                count += 1

        return count


# jewels = "aA"
# stones = "aAAbbbb"
#
# print(set(jewels), set(stones))
# a = [1, 2, 3, 4, 5]

print(sum(i for i in a))
print([i for i in a])
print([s in jewels for s in stones])
print(sum(s in jewels for s in stones))
