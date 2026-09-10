from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        need = Counter(c.lower() for c in licensePlate if c.isalpha())

        answer = None

        for word in words:
            count = Counter(word.lower())

            if all(count[c] >= need[c] for c in need):
                if answer is None or len(word) < len(answer):
                    answer = word

        return answer