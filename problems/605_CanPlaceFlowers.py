class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if(flowerbed[i] == 0):
                if (flowerbed[i-1] == 1 or flowerbed[i+1] == 1):
                    pass
                else:
                    flowerbed[i] = 1
                    count = count + 1

        return count >= n