def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:  # Edge cells
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])

    # The area of the largest square
    return max_side ** 2

# Example usage:
matrix = [
    ['1', '0', '1', '1', '1'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]
print(maximalSquare(matrix))

mtx = [[], ["0", "0", "0", "0"], ["1", "1", "1", "1"], [["1"], ["0"], ["1"], ["1"]], [
    ["0", "0"],
    ["0", "0"]
], [
    ["1", "1"],
    ["1", "1"]
], [
    ["1", "0", "1"],
    ["0", "1", "0"],
    ["1", "0", "1"]
], [
    ["1", "1", "1", "0"],
    ["1", "1", "1", "0"],
    ["1", "1", "1", "1"]
], [
    ["1", "0", "0", "0"],
    ["0", "0", "1", "0"],
    ["0", "1", "0", "0"]
], [
    ["1", "1", "1"],
    ["1", "1", "1"]
], [["0"]], [["1"]], [
    ["1", "1", "1", "0"],
    ["1", "1", "0", "0"],
    ["1", "1", "1", "1"],
    ["0", "1", "1", "1"]
], [["0"] * 100 for _ in range(100)], [["1"] * 100 for _ in range(100)], ]
for matrix in mtx:
    print(maximalSquare(matrix))  # Output: 9
