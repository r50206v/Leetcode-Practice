class Solution(object):
    def addToArrayForm(self, A, K):
        A[-1] += K
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = list(map(int, str(carry))) + A
        return A