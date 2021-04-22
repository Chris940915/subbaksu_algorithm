
# 행렬 회전 :  NxN 행렬이 있다. 이 행렬을 오른쪽으로 90도, 180도, 270도 회전시키는 코드를 작성하라.


def rotate_90(matrix):
    n = len(matrix)
    result = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            result[col][n-row-1] = matrix[row][col]
    return result
        
def rotate_180(matrix):
    n = len(matrix)
    result = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            result[n-1-row][n-1-col] = matrix[row][col]

    return result

def rotate_270(matrix):
    n = len(matrix)
    result = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            result[n-1-col][row] = matrix[row][col]

    return result


test = [[1,2,3], [4,5,6], [7,8,9]]

print("rotate 90 : ", rotate_90(test))
print("rotate 180 : ", rotate_180(test))
print("rotate 270 : ", rotate_270(test))

