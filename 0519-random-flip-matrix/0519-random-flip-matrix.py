import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self) -> list[int]:
        r = random.randrange(self.total)

       
        x = self.map.get(r, r)

       
        last = self.total - 1
        self.map[r] = self.map.get(last, last)

        self.total -= 1

        return [x // self.n, x % self.n]

    def reset(self) -> None:
        self.total = self. m * self.n
        self.map.clear()