class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []  # List to store factors
        
        # Iterate only up to sqrt(n)
        for i in range(1, int(n**0.5) + 1):  
            if n % i == 0:  # If i is a factor of n
                factors.append(i)
                if i != n // i:  # Avoid duplicate when n is a perfect square
                    factors.append(n // i)

        # Sort factors in ascending order
        factors.sort()
        
        # Return the k-th factor if it exists
        return factors[k-1] if k <= len(factors) else -1

# # Example Usage
# solution = Solution()
# print(solution.kthFactor(36, 3))  # Output: 3
# print(solution.kthFactor(36, 6))  # Output: 9
# print(solution.kthFactor(36, 9))  # Output: 36
# print(solution.kthFactor(36, 10)) # Output: -1 (no 10th factor)
