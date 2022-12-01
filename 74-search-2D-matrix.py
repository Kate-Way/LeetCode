# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

def search_matrix(matrix, target):
    left = 0
    right = len(matrix) - 1
    while left <= right:
        sub = (left+right)//2
        if min(matrix[sub]) <= target <= max(matrix[sub]):
            sub_left = 0
            sub_right = len(matrix[sub]) - 1
            while sub_left <= sub_right:
                mid = (sub_left + sub_right)//2
                if matrix[sub][mid] == target:
                    return True
                elif matrix[sub][mid] > target:
                    sub_right = mid - 1
                else:
                    sub_left = mid + 1
            return False
        elif min(matrix[sub]) >= target:
            right = sub - 1
        else:
            left = sub + 1





