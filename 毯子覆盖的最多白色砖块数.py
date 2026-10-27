class Solution:
    def maximumWhiteTiles(self, tiles: list[list[int]], carpetLen: int) -> int:
        tiles.sort()

        n = len(tiles)
        l = 0
        r = 0
        total = 0
        max_tiles = 0

        while l <= r < n:
            left_bound = tiles[l][0]
            right_bound = left_bound + carpetLen - 1
            if tiles[r][1] <= right_bound:
                total += tiles[r][1] - tiles[r][0] + 1
                max_tiles = max(max_tiles, total)
                r += 1
            else:
                if right_bound >= tiles[r][0]:
                    current = total + (right_bound - tiles[r][0] + 1)
                    max_tiles = max(max_tiles, current)

                total -= tiles[l][1] - tiles[l][0] + 1
                l += 1

        return max_tiles

