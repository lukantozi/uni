import numpy as np


'''
np.random.seed(8)
ran_mat = np.random.randint(10, size=(4, 4))
id_mat = np.identity(4)
print(f"Initial matrix:\n{ran_mat}")
print(f"Identity matrix:\n{id_mat}\n")

# a
addition = np.add(ran_mat, id_mat)
print(f"initial + identity:\n{addition}\n")

# b
matr_sum_nums = ran_mat.sum() + id_mat.sum()
print(f"Sum of all numebrs in both matrices: {matr_sum_nums}\n")

# c
ran_mat_max = ran_mat.max()
print(f"Maximum value in ran_mat: {ran_mat_max}")

# d
eight_row_ranmat = ran_mat.reshape((8, 2))
eight_col_id_mat = id_mat.reshape((2,8))
mult_matrices = np.matmul(ran_mat, id_mat)
print(f"ran_mat with 8 rows 2 cols:\n{eight_row_ranmat}\n")
print(f"id_mat with 8 cols 2 rows:\n{eight_col_id_mat}\n")
print(f"eight_row_ranmat X eight_col_id_mat:\n{mult_matrices}")
print()

# e
print("ran_mat:")
print(ran_mat)
print()
rm_third_col_sum = ran_mat[:, 2].sum()
print("third column:")
print(ran_mat[:, 2])
print()
print(rm_third_col_sum)

print("id_mat:")
print(id_mat)
print()
print("third row:")
idm_third_row = id_mat[2]
print(idm_third_row)
idm_third_row_sum = idm_third_row.sum()
print(idm_third_row_sum)

# f
print(ran_mat)
print()
ran_mat[:, 1] = ran_mat[:, 1] ** 2
print(ran_mat)

# g
hor_stacked = np.hstack((ran_mat, id_mat))
print(hor_stacked)

id_str = id_mat.astype(str)
ran_str = ran_mat.astype(str)
added_str = ran_str + id_str
print(added_str)

a = np.array([[2] * 3] * 2)
b = np.array([[3, 4, 5], [6, 7, 8], [9, 10, 11]])
bt = b.transpose()
print(a)
print()
print(b)
print()
print(bt)
a_bt = np.matmul(a, bt)
print()
print(f"a * b^T = \n{a_bt}")
# np.matmul(a.transpose(), b) wouldn't worksince the dimensions of a is 2x3,
# and b^T is 3x3 and 3x3 @ 2x3 is not allowed
'''
