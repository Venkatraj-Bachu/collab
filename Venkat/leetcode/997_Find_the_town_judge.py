class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_rating = [0] * (n+1)
        for (i,j) in trust:
            trust_rating[i] -= 1
            trust_rating[j] += 1

        for i, rating in enumerate(trust_rating[1:], 1):
            if rating == n-1:
                return i
        return -1