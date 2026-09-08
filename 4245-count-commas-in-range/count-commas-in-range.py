class Solution:
    def countCommas(self, n: int) -> int:
     

        total = 0
        power = 1000
        commas = 1

        while power <= n:
            total += n - power + 1
            power *= 1000
            commas += 1

        return total
        