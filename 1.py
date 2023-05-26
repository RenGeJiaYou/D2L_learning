import numpy as np

x = [1.2, 1.8, 3.1, 4.9, 5.7, 7.1, 8.6, 9.8]
y = [4.5, 5.9, 7.0, 7.8, 7.2, 6.8, 4.5, 2.7]

x1 = x
x2 = [i ** 2 for i in x1]

sum_x1 = sum(x1)
sum_x2 = sum(x2)
sum_y = sum(y)

x1_pow = x2
x2_pow = [i ** 2 for i in x2]

sum_x1_pow = sum(x1_pow)
sum_x2_pow = sum(x2_pow)
sum_x1_x2 = sum(np.array(x1) * np.array(x2))
sum_y_pow = sum([i ** 2 for i in y])
sum_x1_y = sum(np.array(x1) * np.array(y))
sum_x2_y = sum(np.array(x2) * np.array(y))

X = np.array([[len(x), sum_x1, sum_x2], [sum_x1, sum_x1_pow, sum_x1_x2], [sum_x2, sum_x1_x2, sum_x2_pow]])
Y = np.array([sum_y, sum_x1_y, sum_x2_y])

b_hat = np.linalg.inv(X) @ Y
print(b_hat)

# x1 = [i**2 for i in x]
# x2 = [i**2 for i in x1]
# y1 = [i**2 for i in y]
#
# a = np.array(x)
# b = np.array(y)
# print(sum(x1))
# print(sum(a*b))
#
# b_hat = (8*230.42-(42.2*46.4))/((8*291.2)-(42.2**2))
#
# a_hat = 46.4/8 - b_hat*(42.2/8)
#
# print(b_hat)
# print(a_hat)
#
# print("avg x2:",sum(x1)/len(x1))
#
# print(sum(x2))
#
# x1_1 = np.array(x1)
# x2_2 =np.array(x2)
#
# print(sum(x1_1*x2_2))
# print(sum(y1))
#
# print(sum(x1_1*y))